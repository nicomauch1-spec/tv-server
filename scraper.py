import json

# Configuración de canales simplificada: 
# Eliminamos NowEvents para priorizar estabilidad con ExoPlayer (StreamTP y La14HD)

CANALES_CONFIG = [
    {
        "id": "0", 
        "name": "ESPN Premium",
        "logoUrl": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/argentina/espn-premium-ar.png",
        "sources": [
            {
                "name": "Opción 1 (HD)", 
                "url": "https://streamtp10.com/global1.php?stream=espnpremium", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 2 (Alternativa)", 
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
                "name": "Opción 1 (HD)", 
                "url": "https://streamtp10.com/global1.php?stream=tntsports", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 2 (Alternativa)", 
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
                "name": "Opción 1 (HD)", 
                "url": "https://streamtp10.com/global1.php?stream=tycsports", 
                "referer": "https://streamtp10.com/"
            },
            {
                "name": "Opción 2 (Alternativa)", 
                "url": "https://la14hd.com/vivo/canales.php?stream=tycsports", 
                "referer": "https://la14hd.com/"
            }
        ]
    }
]

try:
    with open('canales.json', 'w', encoding='utf-8') as f:
        # ensure_ascii=False para que los tildes se vean correctamente
        json.dump(CANALES_CONFIG, f, indent=4, ensure_ascii=False)
    print("✅ canales.json actualizado: Ahora solo con fuentes estables (ExoPlayer).")
except Exception as e:
    print(f"❌ Error al guardar: {e}")
