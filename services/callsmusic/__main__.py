from pyrogram import filters
from service.callsmusic.callsmusic import client
from service.callsmusic.callsmusic import group_call_instances
from services.queues import queues


@client.on_message(filters.me & filters.command("start"))
async def pl(__, _):
    if _.chat.id in group_call_instances.active_chats:
        queues.put(_.chat.id, 'out.raw')
    else:
        await group_call_instances.set_stream(_.chat.id, 'out.raw')


@client.on_message(filters.me & filters.command("end"))
async def pl(__, _):
    await group_call_instances.stop(_.chat.id)

client.run()
