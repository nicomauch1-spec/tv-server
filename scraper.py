import requests
import json
import time
from datetime import datetime, timedelta
from urllib.parse import urlparse

# ==========================================
# CONFIGURACIÓN DEL SCRAPER DE CANALES
# ==========================================

# Mantenemos tu plantilla base. "search_name" ahora será un fragmento que buscaremos dentro de las "options"
MIS_CANALES_BASE = [
    {"id": "0", "name": "ESPN Premium", "search_name": "ESPN Premium", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png"},
    {"id": "1", "name": "TNT Sports", "search_name": "TNT Sports", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png"},
    {"id": "2", "name": "TyC Sports", "search_name": "TyC Sports", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png"},
    {"id": "3", "name": "ESPN", "search_name": "ESPN 1", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-ar.png"},
    {"id": "4", "name": "ESPN 2", "search_name": "ESPN 2", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/refs/heads/main/countries/argentina/espn-2-ar.png"},
    {"id": "5", "name": "ESPN 3", "search_name": "ESPN 3", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/refs/heads/main/countries/argentina/espn-3-ar.png"},
    {"id": "6", "name": "ESPN 4", "search_name": "ESPN 4", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/espn-4-br.png"},
    {"id": "7", "name": "ESPN 5", "search_name": "ESPN 5", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/espn-5-br.png"},
    {"id": "8", "name": "ESPN 6", "search_name": "ESPN 6", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-latin-america/espn-6-lam.png"},
    {"id": "9", "name": "ESPN 7", "search_name": "ESPN 7", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-latin-america/espn-7-lam.png"},
    {"id": "10", "name": "FOX Sports", "search_name": "FOX Sports", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/fox-sports-ar.png"},
    {"id": "11", "name": "FOX Sports 2", "search_name": "FOX Sports 2", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/fox-sports-2-ar.png"},
    {"id": "12", "name": "FOX Sports Premium MX", "search_name": "FOX Sports Premium", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/mexico/fox-sports-premium-mx.png"}, # Le saqué "Mexico" para que coincida más fácil
    {"id": "13", "name": "Premiere 1", "search_name": "Premiere 1", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/premiere-br.png"},
    {"id": "14", "name": "DAZN F1", "search_name": "DAZN F1", "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/spain/dazn-f1-es.png"}
]

PROVEEDORES_PERMITIDOS = ['la14hd', 'streamtpcloud', 'nebunexa', 'bolaloca']
PALABRAS_PROHIBIDAS = ['pc', 'extension', 'vpn', 'app']

def obtener_referer(url):
    try:
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}/"
    except:
        return ""

def es_opcion_valida(opcion):
    nombre_opcion = opcion.get('name', '').lower()
    url_opcion = opcion.get('iframe', '').lower()

    if not url_opcion or url_opcion == 'undefined':
        return False

    for palabra in PALABRAS_PROHIBIDAS:
        if palabra in nombre_opcion:
            return False

    for proveedor in PROVEEDORES_PERMITIDOS:
        if proveedor in url_opcion:
            return True
            
    return False

def procesar_canales():
    print("\n📺 Iniciando scraper de CANALES...")
    timestamp = int(time.time() * 1000)
    url_origen = f"https://nowfutbol.pages.dev/channels.json?{timestamp}"
    
    canales_finales = []
    
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url_origen, headers=headers, timeout=15)
        response.raise_for_status()
        data_origen = response.json()
        
        for mi_canal in MIS_CANALES_BASE:
            fuentes_limpias = []
            urls_vistas = set() # Usamos un Set para evitar duplicados si un canal está en varias "ligas"
            contador_fuentes = 1

            # Buscamos en TODAS las categorías y en TODAS las opciones
            for categoria in data_origen:
                opciones_crudas = categoria.get("options", [])
                
                for opcion in opciones_crudas:
                    nombre_opcion_crudo = opcion.get("name", "")
                    
                    # Verificamos si el nombre de la opción contiene el nombre que buscamos
                    # Ej: Si buscamos "ESPN Premium", tiene que coincidir con "ESPN Premium - Opción 1"
                    if mi_canal["search_name"].lower() in nombre_opcion_crudo.lower():
                        if es_opcion_valida(opcion):
                            url_limpia = opcion.get("iframe")
                            
                            # Evitamos agregar la misma URL dos veces
                            if url_limpia not in urls_vistas:
                                urls_vistas.add(url_limpia)
                                
                                nombre_bonito = f"Opción {contador_fuentes}"
                                if "la14hd" in url_limpia: nombre_bonito += " (Alternativa)"
                                elif "streamtpcloud" in url_limpia: nombre_bonito += " (HD)"
                                elif "nebunexa" in url_limpia: nombre_bonito += " (Nebunexa)"
                                elif "bolaloca" in url_limpia: nombre_bonito += " (Bolaloca)"

                                fuente = {
                                    "name": nombre_bonito,
                                    "url": url_limpia,
                                    "referer": obtener_referer(url_limpia)
                                }
                                fuentes_limpias.append(fuente)
                                contador_fuentes += 1

            # Si encontramos al menos una fuente para este canal, lo guardamos
            if fuentes_limpias:
                nuevo_canal = {
                    "id": mi_canal["id"],
                    "name": mi_canal["name"],
                    "logoUrl": mi_canal["logoUrl"],
                    "sources": fuentes_limpias
                }
                canales_finales.append(nuevo_canal)
                print(f"[+] Canal actualizado: {mi_canal['name']} ({len(fuentes_limpias)} fuentes)")
            else:
                print(f"[-] Canal {mi_canal['name']} sin fuentes válidas.")

        # Guardamos todo el archivo JSON al final
        with open("canales.json", "w", encoding="utf-8") as f:
            json.dump(canales_finales, f, indent=4, ensure_ascii=False)
        print("✅ canales.json guardado con éxito.")

    except Exception as e:
        print(f"❌ Error actualizando canales: {e}")

# ==========================================
# CONFIGURACIÓN DEL SCRAPER DE AGENDA
# ==========================================
LIGAS_TOP = [
    "LIGA PROFESIONAL", "COPA ARGENTINA", "LIBERTADORES", "SUDAMERICANA",
    "PREMIER", "LALIGA", "SERIE A", "BUNDESLIGA", "LIGUE 1", 
    "UEFA Champions League", "EUROPA LEAGUE"
]

def ajustar_hora(hora_str):
    try:
        hora_limpia = hora_str.strip()
        hora_obj = datetime.strptime(hora_limpia, "%H:%M")
        nueva_hora = hora_obj + timedelta(hours=2)
        return nueva_hora.strftime("%H:%M")
    except:
        return hora_str

def procesar_agenda():
    print("\n⚽ Iniciando scraper de AGENDA...")
    url_agenda = "https://la14hd.com/eventos/json/agenda123.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url_agenda, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"📡 Datos recibidos: {len(data)} eventos encontrados en la web.")
        
        agenda_filtrada = []
        partidos_vistos = set()

        for evento in data:
            titulo_raw = evento.get("title", "")
            titulo_up = titulo_raw.upper()
            
            es_cuervo = "SAN LORENZO" in titulo_up
            es_interesante = any(liga in titulo_up for liga in LIGAS_TOP)

            if es_interesante or es_cuervo:
                hora_arg = ajustar_hora(evento.get("time", "00:00"))
                
                clave = f"{titulo_up}-{hora_arg}"
                if clave not in partidos_vistos:
                    partidos_vistos.add(clave)
                    
                    if ":" in titulo_raw:
                        liga, partido = titulo_raw.split(":", 1)
                    else:
                        liga, partido = "Fútbol", titulo_raw

                    agenda_filtrada.append({
                        "liga": liga.strip(),
                        "partido": partido.strip(),
                        "hora": hora_arg,
                        "prioridad": es_cuervo
                    })

        agenda_filtrada.sort(key=lambda x: (not x['prioridad'], x['hora']))

        if not agenda_filtrada:
            print("⚠️ Filtro aplicado: No se encontraron partidos que coincidan con tus ligas.")
        
        with open("partidos.json", "w", encoding="utf-8") as f:
            json.dump(agenda_filtrada, f, indent=4, ensure_ascii=False)
        
        print(f"✅ partidos.json guardado con éxito. ({len(agenda_filtrada)} partidos)")

    except Exception as e:
        print(f"❌ Error actualizando agenda: {e}")

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
def procesar_todo():
    print("🚀 Iniciando actualización general...")
    procesar_canales()
    procesar_agenda()
    print("\n🏁 Proceso terminado.")

if __name__ == "__main__":
    procesar_todo()
