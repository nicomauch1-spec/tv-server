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
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn2-ar.png",
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
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn3-ar.png",
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

if __name__ == "__main__":

    with open("canales.json", "w", encoding="utf-8") as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

    print("✅ canales.json generado correctamente")

