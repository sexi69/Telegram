import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "11975452")
    API_HASH = getenv("API_HASH", "b74516988d4d8ec12efbf56324b80cf5")
    TOKEN = getenv("TOKEN", "5746008573:AAHk9t2qr5qwP_gk41hCDfIRxTIgixyORFI")
    OWNER_ID = getenv("OWNER_ID", "5307865914")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOLkBu7Um62VDHVD-dLFyqzTFKl8hD28v1Qpb7Z6tM3mphIXcBlsbIhu8kuymkAT2NwhuPuhF1ztpFm_xk6v2yjsQcAimRNN81V1cuoLb0LadSz1lDQ5_e5IylV7jvrmXzi2kFbFMIk1H4Bl-rBCDAu_5M8oGIoIk06tQm6ebgT8X474xiJMrmP5ujAJ-UX2Kc0qsIpoXq3iOcfe2bdXWuOOYew9q5BKw9l61SWgPGcvE_ay47X33C55P0VnNeivkc_GJbpE63ydWiHJct__-6SCWKCFZev77mjT1uhzZfYhAMZnB9GB8GSNANVDg639LE22JS5ijny1FlBlc9W7K_2XI0Mk=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Itzaadityaxd")
    DB_URI = getenv("DATABASE_URL", "mongodb+srv://starxrobo:starxrobo@cluster0.efstcnr.mongodb.net/?retryWrites=true&w=majority")
    DB_URI = DB_URI.replace("postgres", "postgres://ovgsprgz:53kb-OVwyUsc0hSlGnnERFxu4gQbEm3E@peanut.db.elephantsql.com/ovgsprgz")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001738358143")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001713781379")
    SYS_ADMIN = getenv("SYS_ADMIN", "5307865914")
    DEV_USERS = getenv("DEV_USERS", "5307865914")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
