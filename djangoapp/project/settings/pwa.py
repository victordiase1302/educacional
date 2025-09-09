from .environment import BASE_DIR

PWA_APP_NAME = "Daniel Fortune"
PWA_APP_DESCRIPTION = "Maior especialista em jogos de slots"
PWA_APP_THEME_COLOR = "#673ab7"
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [
    {
        "src": "/static/images/fav-emoji.png",
        "sizes": "170x170",
        "type": "image/png",
    }
]
PWA_APP_ICONS_APPLE = [
    {
        "src": "/static/images/fav-emoji.png",
        "sizes": "170x170",
        "type": "image/png",
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/images/splash-640x1136.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)", # noqa
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "pt-BR"
PWA_APP_SHORTCUTS = [
    {
        "name": "Shortcut",
        "url": "/",
        "description": "Atalho para o APP",
    }
]
PWA_APP_SCREENSHOTS = [
    {
        "src": "/static/images/splash-750x1334.png",
        "sizes": "750x1334",
        "type": "image/png",
    }
]

PWA_SERVICE_WORKER_PATH = BASE_DIR / "serviceworker.js"
