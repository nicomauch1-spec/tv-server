import json
import re
import cloudscraper


# --- CONFIGURACIÓN DE LIGAS ---
LIGAS_INTERES = [
    "liga profesional", "copa argentina", "libertadores",
    "sudamericana", "champions league", "premier league",
    "laliga", "serie a", "bundesliga", "ligue 1"
]


API_URL = "https://api.promiedos.com.ar/games/today"
WEB_URL = "https://www.promiedos.com.ar"


def obtener_xver_dinamico(scraper):
    print("🔎 Buscando x-ver dinámicamente...")

    try:
        resp = scraper.get(WEB_URL, timeout=20)
        html = resp.text

        # Busca algo como x-ver":"1.11.7.5"
        match = re.search(r'x-ver["\']?\s*[:=]\s*["\']([\d\.]+)', html)

        if match:
            nuevo_xver = match.group(1)
            print(f"✅ x-ver detectado automáticamente: {nuevo_xver}")
            return nuevo_xver

        # Fallback: buscar versión tipo 1.11.7.5 en scripts
        match_alt = re.search(r'(\d+\.\d+\.\d+\.\d+)', html)
        if match_alt:
            posible = match_alt.group(1)
            print(f"⚠️ x-ver alternativo detectado: {posible}")
            return posible

    except Exception as e:
        print(f"❌ Error buscando x-ver dinámico: {e}")

    return None


def llamar_api(scraper, xver):
    headers = {
        "x-ver": xver,
        "origin": WEB_URL,
        "referer": WEB_URL + "/",
        "user-agent": "Mozilla/5.0"
    }

    response = scraper.get(API_URL, headers=headers, timeout=20)
    return response


def obtener_agenda():
    scraper = cloudscraper.create_scraper()

    xver_actual = "1.11.7.5"  # Valor inicial conocido

    print(f"🚀 Intentando API con x-ver: {xver_actual}")

    response = llamar_api(scraper, xver_actual)

    # Si falla, intentamos detectar nuevo x-ver
    if response.status_code != 200:
        print("⚠️ API falló. Intentando detectar nuevo x-ver...")
        nuevo_xver = obtener_xver_dinamico(scraper)

        if nuevo_xver:
            response = llamar_api(scraper, nuevo_xver)
            xver_actual = nuevo_xver
        else:
            print("❌ No se pudo detectar x-ver automáticamente.")
            return []

    print(f"🌐 Status Code final: {response.status_code}")

    if response.status_code != 200:
        print("❌ La API sigue fallando.")
        return []

    try:
        data = response.json()
    except Exception:
        print("❌ Error al decodificar JSON.")
        return []

    # Detectar estructura
    if isinstance(data, list):
        partidos_api = data
    elif isinstance(data, dict):
        partidos_api = (
            data.get("games")
            or data.get("data")
            or data.get("matches")
            or []
        )
    else:
        partidos_api = []

    print(f"🔎 Partidos recibidos: {len(partidos_api)}")

    partidos_hoy = []

    for partido in partidos_api:

        league_data = partido.get("league") or {}
        home_data = partido.get("home") or {}
        away_data = partido.get("away") or {}

        liga = league_data.get("name", "")
        hora = partido.get("time") or partido.get("date") or ""
        local = home_data.get("name", "")
        visitante = away_data.get("name", "")

        if not liga:
            continue

        if any(liga_interes in liga.lower() for liga_interes in LIGAS_INTERES):

            partidos_hoy.append({
                "liga": liga,
                "hora": hora,
                "local": local,
                "visitante": visitante,
                "tv": "A confirmar",
                "prioridad": "san lorenzo" in f"{local} {visitante}".lower()
            })

    partidos_hoy.sort(key=lambda x: x["prioridad"], reverse=True)

    print(f"✅ Partidos filtrados: {len(partidos_hoy)}")

    return partidos_hoy


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

    print("🚀 Iniciando actualización...\n")

    with open('canales.json', 'w', encoding='utf-8') as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

    agenda = obtener_agenda()

    with open('partidos.json', 'w', encoding='utf-8') as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

    print(f"\n🏁 Proceso terminado. Partidos guardados: {len(agenda)}")
