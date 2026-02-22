import json
import requests
from bs4 import BeautifulSoup

# --- CONFIGURACIÓN DE LIGAS (Filtro por palabras clave) ---
# Usamos palabras clave para que no importe si dice "Liga Profesional" o "Liga Profesional Argentina"
LIGAS_INTERES = [
    "liga profesional", "copa argentina", "libertadores", 
    "sudamericana", "champions league", "premier league", 
    "laliga", "serie a", "bundesliga", "ligue 1"
]

def obtener_agenda():
    url = "https://www.promiedos.com.ar/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        partidos_hoy = []

        print("--- 🔍 Iniciando Escaneo de Agenda ---")

        # Buscamos todos los contenedores de ligas (usando coincidencia parcial de clase)
        # Esto soluciona el problema de las clases con códigos como 'jJv13'
        bloques_ligas = soup.find_all('div', class_=lambda x: x and 'match-info_itemevent' in x)

        if not bloques_ligas:
            # Si el diseño moderno falla, probamos con el diseño clásico de Promiedos
            bloques_ligas = soup.find_all('div', class_='tituloinfo')

        for bloque in bloques_ligas:
            # Buscamos el nombre de la liga dentro de una imagen (alt) o un link (text)
            # Esto es lo que vimos en tu captura 'image_80461d.png'
            tag_img = bloque.find('img', alt=True)
            nombre_liga = tag_img['alt'] if tag_img else bloque.get_text(strip=True)

            # Filtramos por tus ligas de interés
            if any(liga.lower() in nombre_liga.lower() for liga in LIGAS_INTERES):
                print(f"✅ Procesando: {nombre_liga}")
                
                # Buscamos los partidos. Suelen estar en tablas (tr) o divs internos
                filas = bloque.find_all(['tr', 'div'], class_=lambda x: x and 'match-info_match' in x)
                
                # Si no encuentra por clase, buscamos todas las filas de tabla
                if not filas: filas = bloque.find_all('tr')

                for fila in filas:
                    celdas = fila.find_all('td')
                    if len(celdas) >= 4:
                        local = celdas[2].get_text(strip=True).replace(' (L)', '').replace(' (V)', '')
                        visitante = celdas[4].get_text(strip=True).replace(' (L)', '').replace(' (V)', '')
                        
                        partido = {
                            "liga": nombre_liga,
                            "hora": celdas[0].get_text(strip=True),
                            "local": local,
                            "visitante": visitante,
                            "tv": celdas[5].get_text(strip=True) if len(celdas) > 5 else "A confirmar",
                            "prioridad": "San Lorenzo" in [local, visitante] or "Liverpool" in [local, visitante]
                        }
                        partidos_hoy.append(partido)

        # San Lorenzo y Liverpool primero
        partidos_hoy.sort(key=lambda x: x['prioridad'], reverse=True)
        return partidos_hoy

    except Exception as e:
        print(f"❌ Error crítico: {e}")
        return []

# --- TU CONFIGURACIÓN DE CANALES (INTACTA) ---
CANALES_CONFIG = [
    {
        "id": "0", 
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "sources": [
            {"name": "Opción 1 (HD)", "url": "https://streamtp501.com/global1.php?stream=espnpremium", "referer": "https://streamtp501.com/"},
            {"name": "Opción 2 (Alternativa)", "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium", "referer": "https://la14hd.com/"},
            {"name": "Opción 3 (Nebunexa)", "url": "https://nebunexa.life/cvatt.html?get=Rm94X1Nwb3J0c19QcmVtaXVu_hE&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 4 (Bolaloca)", "url": "https://bolaloca.my/player/1/76", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "1", 
        "name": "TNT Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png",
        "sources": [
            {"name": "Opción 1 (HD)", "url": "https://streamtp501.com/global1.php?stream=tntsports", "referer": "https://streamtp501.com/"},
            {"name": "Opción 2 (Alternativa)", "url": "https://la14hd.com/vivo/canales.php?stream=tntsports", "referer": "https://la14hd.com/"},
            {"name": "Opción 3 (Nebunexa)", "url": "https://nebunexa.life/cvatt.html?get=VE5UX1Nwb3J0c19IRA&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 4 (Bolaloca)", "url": "https://bolaloca.my/player/1/75", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "2", 
        "name": "TyC Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png",
        "sources": [
            {"name": "Opción 1 (HD)", "url": "https://streamtp501.com/global1.php?stream=tycsports", "referer": "https://streamtp501.com/"},
            {"name": "Opción 2 (Alternativa)", "url": "https://la14hd.com/vivo/canales.php?stream=tycsports", "referer": "https://la14hd.com/"},
            {"name": "Opción 3 (Nebunexa)", "url": "https://www.nebunexa.life/cvatt.html?get=VHlDU3BvcnQ&lang=1", "referer": "https://www.nebunexa.life/"},
            {"name": "Opción 4 (Bolaloca)", "url": "https://bolaloca.my/player/1/77", "referer": "https://bolaloca.my/"}
        ]
    }
]

if __name__ == "__main__":
    # Guardar Canales
    with open('canales.json', 'w', encoding='utf-8') as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)
    
    # Guardar Agenda
    agenda = obtener_agenda()
    with open('partidos.json', 'w', encoding='utf-8') as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

    print(f"✅ Proceso terminado. Se guardaron {len(agenda)} partidos.")
