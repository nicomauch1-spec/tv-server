import requests
import re
import json
import time

# --- TUS FUENTES EXACTAS ---
CANALES_CONFIG = [
    {
        "nombre": "ESPN Premium",
        "logo": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "fuentes": [
            {"nombre": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=ESPN+Premium&o=0"},
            {"nombre": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=espnpremium"},
            {"nombre": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium"}
        ]
    },
    {
        "nombre": "TNT Sports",
        "logo": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png",
        "fuentes": [
            {"nombre": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=0"},
            {"nombre": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tntsports"},
            {"nombre": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tntsports"},
            {"nombre": "Opción 4 (NowEvents Alt)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=6"}
        ]
    },
    {
        "nombre": "TyC Sports",
        "logo": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png",
        "fuentes": [
            {"nombre": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TyC+Sports&o=0"},
            {"nombre": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tycsports"},
            {"nombre": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tycsports"}
        ]
    }
]

# Cabeceras para no ser bloqueados
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://google.com/',
    'Accept': '*/*'
}

def extraer_link_magico(url_web):
    try:
        print(f"   > Escaneando: {url_web}...")
        # 1. Ajustar Referer según la web (truco para StreamTP y NowEvents)
        mis_headers = HEADERS.copy()
        if "streamtp" in url_web:
            mis_headers['Referer'] = "https://streamtp10.com/"
        elif "nowevents" in url_web:
            mis_headers['Referer'] = "https://nowevents.xyz/"

        response = requests.get(url_web, headers=mis_headers, timeout=10)
        html = response.text

        # 2. BUSCAR PATRÓN .m3u8 (HLS)
        # Busca enlaces que empiecen con http y terminen en .m3u8 (incluyendo tokens)
        match_m3u8 = re.search(r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)', html)
        if match_m3u8:
            return match_m3u8.group(1)

        # 3. BUSCAR PATRÓN .mpd (DASH - Mejor calidad)
        match_mpd = re.search(r'(https?://[^\s"\'<>]+\.mpd[^\s"\'<>]*)', html)
        if match_mpd:
            return match_mpd.group(1)

    except Exception as e:
        print(f"   x Error conectando: {e}")
    
    return None

# --- PROGRAMA PRINCIPAL ---
print("--- INICIANDO ROBOT ACTUALIZADOR ---")
lista_final = []
id_contador = 0

for canal_info in CANALES_CONFIG:
    print(f"\nProcesando: {canal_info['nombre']}")
    
    # Preparamos el objeto del canal
    canal_obj = {
        "id": str(id_contador),
        "name": canal_info['nombre'],
        "logoUrl": canal_info['logo'],
        "sources": []
    }
    
    # Probamos cada una de las opciones que pasaste
    for fuente in canal_info['fuentes']:
        link_final = extraer_link_magico(fuente['url'])
        
        if link_final:
            print(f"   ✅ ENCONTRADO: {fuente['nombre']}")
            # Guardamos la opción funcionando
            opcion = {
                "name": fuente['nombre'],
                "url": link_final,
                "referer": fuente['url'] # Guardamos la web original como referer por seguridad
            }
            canal_obj['sources'].append(opcion)
        else:
            print(f"   ❌ FALLÓ: {fuente['nombre']}")
            # Opcional: Podríamos guardar la URL web como respaldo para el 'Espía' si falla la extracción
            # Pero mejor dejarlo limpio por ahora.

    # Solo agregamos el canal si encontramos al menos 1 fuente
    if canal_obj['sources']:
        lista_final.append(canal_obj)
        id_contador += 1
    else:
        print(f"⚠️ ATENCIÓN: No se encontró ninguna fuente para {canal_info['nombre']}")

# Guardamos el JSON
with open('canales.json', 'w', encoding='utf-8') as f:
    json.dump(lista_final, f, indent=4)

print("\n--- ¡LISTO! ARCHIVO canales.json ACTUALIZADO ---")