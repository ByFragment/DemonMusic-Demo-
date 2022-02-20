import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    BOT_NAME = os.environ.get("BOT_NAME")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))