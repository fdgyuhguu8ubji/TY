import os, time
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env', override=True)

class Config(object):
    ##API_KEY get it from dev, dont edit if added
    API_KEY = os.environ.get("API_KEY", "No Need🤣🤣🤣🤣 Edited By Aryan Chaudhary ")
    #telegram user session str for 4gb limit
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
    #tg bot token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ":")
    #api id and hash get it from my.telegram.org
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    PROXY = os.environ.get("PROXY", "")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")
    OWNER_ID = [int(i) for i in  os.environ.get("OWNER_ID", "").split(" ")]
    #log channel, where to send logs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    #gdrive folder id for upload
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1-geGQG9k7_idJ0876uDYqTe")
    #use service accounts or not, used to bypass daily upload limit
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS","False")
    #is team drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "True")
    #index url of gdrive folder
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://widewine.example.workers.dev/0:/BOT")
    HOTSTAR_USER_TOKEN = os.environ.get("HOTSTAR_USER_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..b-0jYVt1xRF6JhqZwyDFchtnfRCy0-jSBruKXY-95hY")
    HOTSTAR_DEVICE_ID = ""

    ZEE5_TOKEN = os.environ.get("ZEE5_TOKEN", "..")

    END_NAME = os.environ.get("END_NAME", "OTT_DOWNLOADER_1BOT")
    METADATA_NAME = os.environ.get("METADATA_NAME", "@TY009X")
    TEMP_DIR = os.environ.get("TEMP_DIR", "output")
    TG_SPLIT_SIZE = int(os.environ.get("TG_SPLIT_SIZE","2000000000"))
    if SESSION_STRING == "" or SESSION_STRING is None:
        TG_SPLIT_SIZE = TG_SPLIT_SIZE
    USE_SERVICE_ACCOUNTS = USE_SERVICE_ACCOUNTS.lower() == "true"
    IS_TEAM_DRIVE = IS_TEAM_DRIVE.lower() == "true"
    HOTSTAR_REFRESH = time.time()