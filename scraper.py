import json
import requests
from bs4 import BeautifulSoup

# --- CONFIGURACIÓN DE LIGAS (Las que pediste de Promiedos) ---
LIGAS_PERMITIDAS = [
    "Liga Profesional", "Copa Argentina", 
    "CONMEBOL Copa Libertadores", "CONMEBOL Copa Sudamericana",
    "Champions League", "Premier League", "LaLiga", 
    "Serie A", "Bundesliga", "Ligue 1"
]

def obtener_agenda():
    url = "https://www.promiedos.com.ar/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        partidos_hoy = []

        # Buscamos los bloques de ligas
        for tabla in soup.select('div[id^="fixturein"]'):
            titulo_liga = tabla.find_previous('div', class_='tituloinfo')
            if not titulo_liga: continue
            
            nombre_liga = titulo_liga.get_text(strip=True)

            # Filtramos solo tus ligas favoritas
            if any(liga in nombre_liga for liga in LIGAS_PERMITIDAS):
                for fila in tabla.select('tr'):
                    celdas = fila.find_all('td')
                    if len(celdas) >= 4:
                        local = celdas[2].get_text(strip=True)
                        visitante = celdas[4].get_text(strip=True)
                        
                        partido = {
                            "liga": nombre_liga,
                            "hora": celdas[0].get_text(strip=True),
                            "local": local,
                            "visitante": visitante,
                            "tv": celdas[5].get_text(strip=True) if len(celdas) > 5 else "A confirmar",
                            "prioridad": "San Lorenzo" in [local, visitante] # San Lorenzo arriba
                        }
                        partidos_hoy.append(partido)

        # Ordenamos para que San Lorenzo aparezca primero
        partidos_hoy.sort(key=lambda x: x['prioridad'], reverse=True)
        return partidos_hoy
    except Exception as e:
        print(f"❌ Error en el scraper de agenda: {e}")
        return []

# --- TU CONFIGURACIÓN DE CANALES (Mantenida al 100%) ---
CANALES_CONFIG = [
    {
        "id": "0", 
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "sources": [
            {"name": "Opción 1 (HD)", "url": "https://streamtp501.com/global1.php?stream=espnpremium", "referer": "https://streamtp501.com/"},
            {"name": "Opción 2 (Alternativa)", "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium", "referer": "https://la14hd.com/"},
            {"name": "Opción 3 (Nebunexa)", "url": "https://nebunexa.life/cvatt.html?get=Rm94X1Nwb3J0c19QcmVtaXVuX0hE&lang=1", "referer": "https://nebunexa.life/"},
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

# --- BLOQUE DE EJECUCIÓN (Guarda ambos archivos) ---
if __name__ == "__main__":
    try:
        # 1. Guardar los canales
        with open('canales.json', 'w', encoding='utf-8') as f:
            json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)
        print("✅ canales.json actualizado: Se incluyeron todas las fuentes.")

        # 2. Obtener y guardar la agenda de partidos
        agenda = obtener_agenda()
        with open('partidos.json', 'w', encoding='utf-8') as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)
        print(f"✅ partidos.json actualizado. Se encontraron {len(agenda)} partidos.")

    except Exception as e:
        print(f"❌ Error al guardar archivos: {e}")
