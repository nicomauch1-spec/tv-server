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

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def extraer_link(url_web):
    try:
        # Intentamos extraer el link m3u8 directo
        r = requests.get(url_web, headers=HEADERS, timeout=10)
        match = re.search(r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)', r.text)
        if match: return match.group(1)
    except: pass
    return None

lista_final = []
for canal in CANALES_CONFIG:
    obj_canal = {"id": canal["id"], "name": canal["name"], "logoUrl": canal["logoUrl"], "sources": []}
    for f in canal["fuentes"]:
        link_directo = extraer_link(f["url"])
        # SIEMPRE agregamos la fuente. Si no hay link directo, mandamos la web original.
        obj_canal["sources"].append({
            "name": f["name"],
            "url": link_directo if link_directo else f["url"], 
            "referer": f["url"]
        })
    lista_final.append(obj_canal)

with open('canales.json', 'w', encoding='utf-8') as f:
    json.dump(lista_final, f, indent=4)
