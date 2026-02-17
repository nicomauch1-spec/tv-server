import json

# Configuración con NowEvents como prioridad para aprovechar el ABR (Calidad automática)
CANALES_CONFIG = [
    {
        "id": "0", 
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "sources": [
            {
                "name": "Opción 1 (NowEvents - Auto)", 
                "url": "https://nowevents.xyz/vivo/?c=ESPN+Premium&o=0",
            },
            {
                "name": "Opción 2 (StreamTP)", 
                "url": "https://streamtp10.com/global1.php?stream=espnpremium", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 3 (La14HD)", 
                "url": "https://la14hd.com/vivo/canales.php?stream=espnpremium", 
                "referer": "https://la14hd.com/"
            }
        ]
    },
    {
        "id": "1", 
        "name": "TNT Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tnt-sports-ar.png",
        "sources": [
            {
                "name": "Opción 1 (NowEvents - Auto)", 
                "url": "https://nowevents.xyz/vivo/?c=TNT+Sports&o=0",
            },
            {
                "name": "Opción 2 (StreamTP)", 
                "url": "https://streamtp10.com/global1.php?stream=tntsports", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 3 (La14HD)", 
                "url": "https://la14hd.com/vivo/canales.php?stream=tntsports", 
                "referer": "https://la14hd.com/"
            }
        ]
    },
    {
        "id": "2", 
        "name": "TyC Sports",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/tyc-sports-ar.png",
        "sources": [
            {
                "name": "Opción 1 (NowEvents - Auto)", 
                "url": "https://nowevents.xyz/vivo/?c=TyC+Sports&o=0",
            },
            {
                "name": "Opción 2 (StreamTP)", 
                "url": "https://streamtp10.com/global1.php?stream=tycsports", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 3 (La14HD)", 
                "url": "https://la14hd.com/vivo/canales.php?stream=tycsports", 
                "referer": "https://la14hd.com/"
            }
        ]
    }
]

# Guardamos el archivo canales.json para que la App lo descargue al iniciar
try:
    with open('canales.json', 'w', encoding='utf-8') as f:
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)
    print("✅ canales.json actualizado: NowEvents reincorporado como Opción 1.")
except Exception as e:
    print(f"❌ Error al guardar el archivo: {e}")
