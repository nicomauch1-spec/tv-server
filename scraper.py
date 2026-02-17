import requests
import re
import json

# --- CONFIGURACIÓN ---
CANALES_CONFIG = [
    {
        "id": "0",
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=ESPN+Premium&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=espnpremium"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium"}
        ]
    },
    {
        "id": "1",
        "name": "TNT Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tntsports"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tntsports"},
            {"name": "Opción 4 (NowEvents Alt)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=6"}
        ]
    },
    {
        "id": "2",
        "name": "TyC Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TyC+Sports&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tycsports"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tycsports"}
        ]
    }
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def extraer_link(url_web):
    try:
        # Ajustamos el referer para engañar a la web
        session_headers = HEADERS.copy()
        if "nowevents" in url_web: session_headers["Referer"] = "https://nowevents.xyz/"
        if "streamtp" in url_web: session_headers["Referer"] = "https://streamtp10.com/"
        
        r = requests.get(url_web, headers=session_headers, timeout=10)
        # Buscamos m3u8 o mpd
        match = re.search(r'(https?://[^\s"\'<>]+\.(m3u8|mpd)[^\s"\'<>]*)', r.text)
        
        if match:
            link = match.group(1)
            # ⚠️ CLAVE: Si el link trae la IP de GitHub, lo descartamos.
            # Preferimos que la App use el Espía con la IP real del usuario.
            if "ip=" in link or "token=" in link:
                print(f"   ! Link con token detectado (IP Restringida). Usando modo Sniffer.")
                return None
            return link
    except Exception as e:
        print(f"   x Error en {url_web}: {e}")
    return None

print("--- INICIANDO SCRAPER BLINDADO ---")
lista_final = []

for canal in CANALES_CONFIG:
    print(f"\n> Procesando: {canal['name']}")
    obj_canal = {
        "id": canal["id"],
        "name": canal["name"],
        "logoUrl": canal["logoUrl"],
        "sources": []
    }
    
    for f in canal["fuentes"]:
        link_final = extraer_link(f["url"])
        
        # Si el robot encontró un link 'limpio', se usa. 
        # Si no, se manda la URL de la web para que la App la 'espie' localmente.
        obj_canal["sources"].append({
            "name": f["name"],
            "url": link_final if link_final else f["url"], 
            "referer": f["url"]
        })
        status = "DIRECTO" if link_final else "WEB (SNIFFER)"
        print(f"   + {f['name']}: {status}")
        
    lista_final.append(obj_canal)

# Guardar con formato limpio
with open('canales.json', 'w', encoding='utf-8') as f:
    json.dump(lista_final, f, indent=4, ensure_ascii=False)

print("\n--- PROCESO TERMINADO: canales.json actualizado ---")
