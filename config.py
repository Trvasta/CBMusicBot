import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("BQGjk2UALpvTOlUtMQIo-J586DOK8aveUVKgvrDoza8YwezMXQeZpcO7IgsEtAbugDKbWIia-8cTPWnU7T3IdQcu9XbkB1xvp9Wmw3ctIKhStcWqSlSAUUTM1225zCSXU7knetF1yW67QroGpfK_rgXj35TYThB_REFqeXEiaVZ9r6LGwUBF8EJu9iM0GrnrEYVvCqb3wCr5vSa-8fPlafCOjtmpbFEfnDU1YQ-d52bLkENsiw6UzvzHUZUCkB0fl8kqzg3AueK8l3R08Y5v8pJIlah6EUzY3t3XjFGBXo77QHC_1gyPsrwNBv4gIPWjQob8ksRQFStnBCA1MF53BRm9VQT_GwAAAAGChUkaAA")
BOT_TOKEN = getenv("7221149690:AAGspc1Dw2mnrVqJg1on6bQJPU2IzO5aq00")
BOT_NAME = getenv("OrboroBot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("27497317"))
API_HASH = getenv("912dc329039f9fcf92b6ace0efb35cef")
BOT_USERNAME = getenv("OrboroBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("OrboroBotSupport")
UPDATES_CHANNEL = getenv("ChestChannel")
OWNER_NAME = getenv("Digitio") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("6484740378")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://OrboroBot:OrboroBot@cluster0.tvxqfcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002207392342")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
