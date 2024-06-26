import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=7221149690:AAGspc1Dw2mnrVqJg1on6bQJPU2IzO5aq00,
    plugins=dict(root="handlers"),
)

print("[INFO]: CYBERMUSIC STARTED!")

bot.start()
run()
