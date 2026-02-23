import json
import cloudscraper

# --- CONFIGURACIÓN DE LIGAS ---
LIGAS_INTERES = [
    "liga profesional",
    "copa argentina",
    "libertadores",
    "sudamericana",
    "champions league",
    "premier league",
    "laliga",
    "serie a",
    "bundesliga",
    "ligue 1"
]


def obtener_agenda():

    scraper = cloudscraper.create_scraper(
        browser={
            "browser": "chrome",
            "platform": "windows",
            "mobile": False
        }
    )

    API_URL = "https://api.promiedos.com.ar/games/today"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-AR,es;q=0.9,en;q=0.8",
        "origin": "https://www.promiedos.com.ar",
        "referer": "https://www.promiedos.com.ar/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    }

    try:
        print("🚀 Consultando API Promiedos...")

        response = scraper.get(API_URL, headers=headers, timeout=30)

        print("🌐 Status:", response.status_code)

        if response.status_code != 200:
            print("❌ Error API")
            print(response.text[:500])
            return []

        data = response.json()

        # DEBUG si vuelve vacío
        if not data:
            print("⚠ Respuesta vacía")
            print(response.text[:500])
            return []

        leagues = data.get("leagues", [])

        print(f"🔎 Ligas recibidas: {len(leagues)}")

        partidos_hoy = []

        for liga in leagues:

            nombre_liga = liga.get("name", "")

            # Filtrar solo ligas que nos interesan
            if not any(l in nombre_liga.lower() for l in LIGAS_INTERES):
                continue

            juegos = liga.get("games", [])

            for partido in juegos:

                status = partido.get("status", {})
                status_enum = status.get("enum")

                # ❌ Excluir finalizados
                if status_enum == 3:
                    continue

                equipos = partido.get("teams", [])

                if len(equipos) < 2:
                    continue

                local = equipos[0].get("name", "")
                visitante = equipos[1].get("name", "")
                hora = partido.get("start_time", "")

                estado = status.get("short_name", "")

                tv_networks = partido.get("tv_networks", [])
                tv = ", ".join([t.get("name") for t in tv_networks]) if tv_networks else "A confirmar"

                partidos_hoy.append({
                    "liga": nombre_liga,
                    "hora": hora,
                    "local": local,
                    "visitante": visitante,
                    "estado": estado,
                    "tv": tv,
                    "prioridad": "san lorenzo" in f"{local} {visitante}".lower()
                })

        # 🔥 Orden:
        # 1) San Lorenzo primero
        # 2) En vivo antes que programados
        partidos_hoy.sort(
            key=lambda x: (
                not x["prioridad"],
                x["estado"] != "LIVE"
            )
        )

        print(f"✅ Partidos activos encontrados: {len(partidos_hoy)}")

        return partidos_hoy

    except Exception as e:
        print("❌ Error general:", e)
        return []


# --- CANALES (NO TOCADO) ---
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

    with open("canales.json", "w", encoding="utf-8") as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

    agenda = obtener_agenda()

    with open("partidos.json", "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

    print(f"\n🏁 Proceso terminado. Partidos guardados: {len(agenda)}")
