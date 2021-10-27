import config

from pyrogram import Client
from services.queues import queues
from services.callsmusic.callsmusic import groupcall, run

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run

__all__ = ["queues", "groupcall", "run"]
