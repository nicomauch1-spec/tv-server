import json
import cloudscraper


# --- CONFIGURACIÓN DE LIGAS (Filtro por palabras clave) ---
LIGAS_INTERES = [
    "liga profesional", "copa argentina", "libertadores",
    "sudamericana", "champions league", "premier league",
    "laliga", "serie a", "bundesliga", "ligue 1"
]


def obtener_agenda():
    url = "https://api.promiedos.com.ar/games/today"

    headers = {
        "x-ver": "1.11.7.5",
        "origin": "https://www.promiedos.com.ar",
        "referer": "https://www.promiedos.com.ar/",
        "user-agent": "Mozilla/5.0"
    }

    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url, headers=headers, timeout=20)

        print(f"🌐 Status Code: {response.status_code}")

        if response.status_code != 200:
            print("❌ La API no respondió correctamente")
            return []

        try:
            data = response.json()
        except Exception:
            print("❌ Error al decodificar JSON")
            return []

        # --- Detectar estructura real ---
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

        print(f"🔎 Partidos recibidos desde API: {len(partidos_api)}")

        if not partidos_api:
            print("⚠️ No hay partidos hoy o la estructura cambió.")
            return []

        partidos_hoy = []

        for partido in partidos_api:

            # Protección por si cambian estructura interna
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

        # Prioridad primero
        partidos_hoy.sort(key=lambda x: x["prioridad"], reverse=True)

        print(f"✅ Partidos filtrados guardados: {len(partidos_hoy)}")

        return partidos_hoy

    except Exception as e:
        print(f"❌ Error crítico general: {e}")
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

    print("🚀 Iniciando actualización...\n")

    # Guardar Canales
    with open('canales.json', 'w', encoding='utf-8') as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

    # Guardar Agenda
    agenda = obtener_agenda()

    with open('partidos.json', 'w', encoding='utf-8') as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

    print(f"\n🏁 Proceso terminado. Partidos guardados: {len(agenda)}")
