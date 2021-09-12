# DAISYXMUSIC - Telegram bot project
# RemXmusic (Telegram bot project)
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
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
# Modified by Inukaasith

import os
import re
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAvKXf1GjrjXXg9vrNUoA9fHdsEGSJ_2yGOhtVl6y4i7J-NICOI8tE-V8OGXmzqvkmZCtZPz7VDHaAyBEdrbjEtsQdSMUC8X0XGqdvGhOdPctm4KwZBLynV27PjD3cwEOEEQJoIBTDqS6YQSOTCkyg8N3tk-rfTa5wG3fYyZJqzBo3sxfzY5kw3mAZ2cdoOIWYIPLcpr4ubks6a3peUf_radlkgHEjrx42Jyz_imGe2gsNngUQWRFhyWIQFugrRWhUe6ltdkkNCM8wo0ONAwqTSjno_OgS6q1qOVk-VQ5q-LqGm91azBDB-FNqXftmFvoN93Nh56F7Wvru5f2f8QTafc_w-0wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1928719455:AAEAM3gkCh43QweVsr_KTKeMtkYhMO5RKdg")
BOT_NAME = getenv("BOT_NAME", "Rem Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "queengemoy_project")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9a0bfe8b4b6478c6979a4.png")
admins = {}
API_ID = int(getenv("API_ID", "7703315"))
API_HASH = getenv("API_HASH", "43118491ea08de184cbbcd11a93398ec")
BOT_USERNAME = getenv("BOT_USERNAME", "RemMusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RamMusicAsisstant_bot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "rL1p4FVSWH1mM2E1")
PROJECT_NAME = getenv("PROJECT_NAME", "RemXMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/brut-ctrl/RemXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
DELAY = int(getenv("DELAY", 10))
ARQ_API_KEY = getenv("ARQ_API_KEY", "AUDEEE-WKVNES-UGXHIX-QFDHIU-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
PMMSG = getenv("PMMSG", f"Hi there, This is a music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n")
LOG_GRP = getenv("LOG_GRP", "-1001534925371")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "712147852 1408440765 1944787421 1820831401 1945910995 1909021805 1605366945").split()))
