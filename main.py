from pyrogram import Client as Bot

from services.callsmusic import run
from config import API_ID, API_HASH, BG_IMAGE, BOT_TOKEN, SUDO_USERS
import requests

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="modules")
)
bot.start()
run()
