# RemXmusic (Telegram bot project )
# Copyright (C) 2021  @brut69 (RemXmusic)
# Copyright (C) 2021  Bemro-Official 
# Copyright (C) 2021  Inukaasith (Modified)
# Copyright (C) 2021  Technical-Hunter (Modified)

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

import os
from config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL

class Messages():
      START_MSG = """
**Hello bruh 👋 [{}](tg://user?id={})!**

🤖 I m RemXmusic bot created for playing which music in Channels and Groups.\nI can even Stream Youtube Live in Your Voicechat.\nDeploy Your Own bot from source code below.

👻 Send me /help for more info.
"""
      
      HELP_MSG = [
        ".",
f"""
**Eyyo bruh 👋 Welcome back to {PROJECT_NAME}

⚡ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚡ Assistant @{ASSISTANT_NAME}

Click next for instructions**
""",

f"""
**Setting up**

1) Make bot as admin (Group and in channel if use /cplay)
2) Start a voice chat
3) Try /play <song title> for the first time by an @admin. If userbot joined enjoy music, If not add manualy @{ASSISTANT_NAME} to your group and report issue to Owner bot

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Commands**

**✓ Song Playing 🎵**

- /play - Play the requestd song
- /play <yt url> - Play the given yt url
- /play <reply audio file> - Play replied audio
- /splay - Play song via jio saavn
- /ytplay - Directly play song via Youtube Music

**✓ Playback 🎵**

- /player - Open Settings menu of player
- /skip - Skips the current track
- /pause - Pause track
- /resume - Resume the paused track
- /end - Stops media playback
- /current - Shows the current Playing track
- /playlist - Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**√ Channel Music Play 🎶**

🥰 For linked group admins only

- /cplay <song title> - Play song you requested
- /csplay <song title> - Play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - Open music player settings panel
- /cpause - Pause song play
- /cresume - Resume song play
- /cskip - Play next song
- /cend - Stop music play
- /userbotjoinchannel - Invite assistant to your chat

channel is also can be used instead of c /cplay or /channelplay

🥰 If you donlt like to play in linked group

1) Get your channel ID
2) Add bot as Channel admin with full perms
3) Add @{ASSISTANT_NAME} to the channel as an admin
4) Simply send commands in your group
""",

f"""
**✓ More tools ⚡**

- /musicplayer <on/off> - Enable/disable Music player
- /admincache - Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin - Invite @{ASSISTANT_NAME} Userbot to your chat
- /auth <reply to user> - Authorize User
- /deauth <reply to user> - DeAuthorize user
Authorized users can execute admin commands in authorized group

**✓ Commands for Sudo Users ⚡**

 - /userbotleaveall - Remove assistant from all chats
 - /gcast <reply to message> - Globally brodcast replied message to all chats
 - /pmpermit <on/off> - Enable/disable pmpermit message
- Sudo Users can execute any command in any groups

"""
      ]
