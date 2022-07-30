# Powered by @Dk143gurjar | @Dkgurjar143
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12138418"))
API_HASH = getenv("API_HASH", "f7c60f0f506a54d27df6bc32a1bbe785")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dk143gurjar")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Education_quiz_hub")
BOT_NAME = getenv("BOT_NAME","𝐃𝐊 𝐌𝐔𝐒𝐈𝐂")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/5e31ae87791fdc24d74ae.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1781352356").split()))
