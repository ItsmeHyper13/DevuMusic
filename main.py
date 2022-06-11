# Powered by @being_rohi | 
# Dear Pero ppls Plish Don't remov@mooojooo0e this line from here🌚
# created by mooojooo0

import requests
from pyrogram import idle
from pyrogram import Client as Bot
from callsmusic.callsmusic import client as USER

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

async def main():
    async with bot:
        try:
            await USER.join_chat(TAMILSQUAD)
            await USER.join_chat(being_rohi)
            await USER.join_chat(clownchatters)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            print(e)
            pass

bot.start()
run()
idle()
