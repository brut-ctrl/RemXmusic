# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


#from typing import Dict
from pyrogram import Client
from pytgcalls import GroupCall

from config import API_HASH, API_ID, SESSION_NAME
from services.queues import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = GroupCall(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: GroupCall, chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(chat_id, queues.get(chat_id)["file"])


run = pytgcalls.start
