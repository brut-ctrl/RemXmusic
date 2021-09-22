from services.queues import queues
from pyrogram import Client
import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
