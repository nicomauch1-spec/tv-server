import json

# Usamos la estructura /embed/ que es la que suelta el video rápido
CANALES_CONFIG = [
    {
        "id": "0", 
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "sources": [
            {
                "name": "Opción 1 (NowEvents - Auto)", 
                "url": "https://nowevents.xyz/embed/espn-premium"
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
                "url": "https://nowevents.xyz/embed/tnt-sports"
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
                "url": "https://nowevents.xyz/embed/tyc-sports"
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

with open('canales.json', 'w', encoding='utf-8') as f:
    json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)

print("✅ canales.json corregido con links de Embed.")
