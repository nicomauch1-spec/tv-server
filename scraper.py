import json

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

    print("✅ canales.json generado correctamente")
