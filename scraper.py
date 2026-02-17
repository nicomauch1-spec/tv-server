import requests
import re
import json

# --- CONFIGURACIÓN DE REFERERS (Tus reglas de F12) ---
REFERER_RULES = {
    "nowevents.xyz": "https://nowevents.xyz/",
    "streamtp10.com": "https://streamtp10.com/",
    "la14hd.com": "https://la14hd.com/",
    "fubohd.com": "https://la14hd.com/"
}

CANALES_CONFIG = [
    {
        "id": "0", "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=ESPN+Premium&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=espnpremium"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium"}
        ]
    },
    {
        "id": "1", "name": "TNT Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tntsports"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tntsports"},
            {"name": "Opción 4 (NowEvents Alt)", "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=6"}
        ]
    },
    {
        "id": "2", "name": "TyC Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png",
        "fuentes": [
            {"name": "Opción 1 (NowEvents)", "url": "https://nowevents.xyz/vivo/?c=TyC+Sports&o=0"},
            {"name": "Opción 2 (StreamTP)", "url": "https://streamtp10.com/global1.php?stream=tycsports"},
            {"name": "Opción 3 (La14HD)", "url": "https://la14hd.com/vivo/canales.php?stream=tycsports"}
        ]
    }
]

HEADERS_BASE = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def extraer_m3u8_avanzado(url_web):
    try:
        # 1. Determinar el Referer correcto según el dominio
        referer = None
        for domain, ref in REFERER_RULES.items():
            if domain in url_web:
                referer = ref
                break
        
        h = HEADERS_BASE.copy()
        if referer: h['Referer'] = referer

        # 2. Obtener el HTML
        r = requests.get(url_web, headers=h, timeout=10)
        html = r.text

        # 3. Búsqueda Multi-Patrón (Regex Pro)
        # Busca links .m3u8 o .mpd, incluso si tienen barras invertidas o están en variables JS
        patrones = [
            r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)\'', # Link simple en comillas simples
            r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)\"', # Link simple en comillas dobles
            r'source:\s*["\'](.*?\.m3u8.*?)["\']',         # Variable source de Clappr/Player
            r'file:\s*["\'](.*?\.m3u8.*?)["\']'           # Variable file de JWPlayer
        ]
        
        for p in patrones:
            match = re.search(p, html, re.IGNORECASE)
            if match:
                link = match.group(1).replace('\\/', '/') # Limpiar barras de JS
                return link, referer

    except Exception as e:
        print(f"   x Error: {e}")
    return None, None

# --- EJECUCIÓN ---
print("🚀 Iniciando extracción de alta precisión...")
resultado_json = []

for canal in CANALES_CONFIG:
    print(f"\n📺 {canal['name']}")
    c_entry = {"id": canal["id"], "name": canal["name"], "logoUrl": canal["logoUrl"], "sources": []}
    
    for f in canal["fuentes"]:
        link, ref = extraer_m3u8_avanzado(f["url"])
        
        # Guardamos la data. Si el link falló, guardamos la URL de la web para el Sniffer de la app.
        c_entry["sources"].append({
            "name": f["name"],
            "url": link if link else f["url"],
            "referer": ref if link else f["url"]
        })
        status = "✅ M3U8" if link else "🌍 WEB"
        print(f"   {status} -> {f['name']}")

    resultado_json.append(c_entry)

with open('canales.json', 'w', encoding='utf-8') as f:
    json.dump(resultado_json, f, indent=4, ensure_ascii=False)
print("\n✅ canales.json actualizado con éxito.")
