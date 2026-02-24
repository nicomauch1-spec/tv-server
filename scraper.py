import requests
import json
from datetime import datetime, timedelta

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
    },
    {
        "id": "3",
        "name": "ESPN",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-ar.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=RVNQTjJIRA&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://la14hd.com/vivo/canales.php?stream=espn", "referer": "https://la14hd.com/"},
            {"name": "Opción 3", "url": "https://streamtp501.com/global1.php?stream=espn", "referer": "https://streamtp501.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/87", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "4",
        "name": "ESPN 2",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/refs/heads/main/countries/argentina/espn-2-ar.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=RVNQTjJfQXJn&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn2", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn2", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/88", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "5",
        "name": "ESPN 3",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/refs/heads/main/countries/argentina/espn-3-ar.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=RVNQTjM=&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn2", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn3", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/89", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "6",
        "name": "ESPN 4",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/espn-4-br.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=RVNQTkhE&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn4", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn4", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/90", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "7",
        "name": "ESPN 5",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/espn-5-br.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=RVNQTjQ=&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn5", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn5", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/91", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "8",
        "name": "ESPN 6",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-latin-america/espn-6-lam.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=Rm94U3BvcnRzM19VWQ==&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn6", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn6", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/92", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "9",
        "name": "ESPN 7",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-latin-america/espn-7-lam.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=Rm94U3BvcnRzMl9VWQ==&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=espn7", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=espn7", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/93", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "10",
        "name": "FOX Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/fox-sports-ar.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=Rm94U3BvcnRz&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=fox1ar", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=foxsports", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/78", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "11",
        "name": "FOX Sports 2",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/fox-sports-2-ar.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/cvatt.html?get=Rm94U3BvcnRzMkhE&lang=1", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=fox2ar", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=foxsports2", "referer": "https://la14hd.com/"},
            {"name": "Opción 4", "url": "https://bolaloca.my/player/1/79", "referer": "https://bolaloca.my/"}
        ]
    },
    {
        "id": "12",
        "name": "FOX Sports Premium MX",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/mexico/fox-sports-premium-mx.png",
        "sources": [
            {"name": "Opción 1", "url": "https://bolaloca.my/player/1/104", "referer": "https://bolaloca.my/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=foxsportspremium", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=foxsportspremium", "referer": "https://la14hd.com/"}
        ]
    },
    {
        "id": "13",
        "name": "Premiere 1",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/brazil/premiere-br.png",
        "sources": [
            {"name": "Opción 1", "url": "https://nebunexa.life/mpdk/?get=aHR0cHM6Ly9hYmMzb3J3YWFhYWFhYWFtaHB1aTd3bG5tZnFnaC5vdHRiLmxpdmUuY2Yud3cuYWl2LWNkbi5uZXQvZ3J1LW5pdHJvL2xpdmUvY2xpZW50cy9kYXNoL2VuYy9uZWxmeXVjdzlhL291dC92MS82ZmZiMmMzNjVhZDE0Zjg4YjE1NDU5MWJlYjQzZDFmNi9jZW5jLm1wZA==&key=NTZiNzljMTc4MmIzMGU2YjZmYzk3M2IwZThmZDQxMDQ=&key2=ZmEzOGFhYTg2NWE1N2VkYTdjNzc0NDQ2OTdiYThlZDM=", "referer": "https://nebunexa.life/"},
            {"name": "Opción 2", "url": "https://streamtpcloud.com/global1.php?stream=premiere1", "referer": "https://streamtp501.com/"},
            {"name": "Opción 3", "url": "https://la14hd.com/vivo/canales.php?stream=premiere1", "referer": "https://la14hd.com/"}
        ]
    },
    {
        "id": "14",
        "name": "DAZN F1",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/spain/dazn-f1-es.png",
        "sources": [
            {"name": "Opción 1", "url": "https://bolaloca.my/player/1/60", "referer": "https://bolaloca.my/"}
        ]
    }
]

# --- CONFIGURACIÓN DE AGENDA ---
# He simplificado las palabras clave para que coincidan más fácil
LIGAS_TOP = [
    "LIGA PROFESIONAL", "COPA ARGENTINA", "LIBERTADORES", "SUDAMERICANA",
    "PREMIER", "LALIGA", "SERIE A", "BUNDESLIGA", "LIGUE 1", 
    "CHAMPIONS", "EUROPA LEAGUE", "CONCACAF"
]

def ajustar_hora(hora_str):
    try:
        # Algunos vienen con espacios o formatos raros, limpiamos:
        hora_limpia = hora_str.strip()
        hora_obj = datetime.strptime(hora_limpia, "%H:%M")
        nueva_hora = hora_obj + timedelta(hours=2)
        return nueva_hora.strftime("%H:%M")
    except:
        return hora_str

def procesar_todo():
    print("🚀 Iniciando scraper...")
    
    # 1. Canales
    with open("canales.json", "w", encoding="utf-8") as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

    # 2. Agenda
    url_agenda = "https://la14hd.com/eventos/json/agenda123.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url_agenda, headers=headers, timeout=15)
        data = response.json()
        print(f"📡 Datos recibidos: {len(data)} eventos encontrados en la web.")
        
        agenda_filtrada = []
        partidos_vistos = set()

        for evento in data:
            titulo_raw = evento.get("title", "")
            titulo_up = titulo_raw.upper()
            
            # Buscamos San Lorenzo o las ligas
            es_cuervo = "SAN LORENZO" in titulo_up
            es_interesante = any(liga in titulo_up for liga in LIGAS_TOP)

            if es_interesante or es_cuervo:
                hora_arg = ajustar_hora(evento.get("time", "00:00"))
                
                clave = f"{titulo_up}-{hora_arg}"
                if clave not in partidos_vistos:
                    partidos_vistos.add(clave)
                    
                    # Separar Liga de Equipos
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

        # Ordenar: Prioridad San Lorenzo primero, luego hora
        agenda_filtrada.sort(key=lambda x: (not x['prioridad'], x['hora']))

        # IMPORTANTE: Si después de filtrar no hay nada, avisamos en la consola
        if not agenda_filtrada:
            print("⚠️ Filtro aplicado: No se encontraron partidos que coincidan con tus ligas.")
        
        with open("partidos.json", "w", encoding="utf-8") as f:
            json.dump(agenda_filtrada, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Proceso terminado. Partidos guardados: {len(agenda_filtrada)}")

    except Exception as e:
        print(f"❌ Error crítico: {e}")

if __name__ == "__main__":
    procesar_todo()

