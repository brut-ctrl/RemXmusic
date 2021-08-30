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
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC2a-OmeHBk9ecdqBMqNsRlBo4Zh_dAY4MGfZOn98WLvxdDs25Px4YQ7ykfs0wU3ijHusnE0o5GD5PFXiOu0q5EQu7QF0MpCvnAzdK8xSPNkTmC-3Dy8xwtjM6erefw3g8C1BLbkqjaxTI2DBJqETpNLMA9By9sWqS37hZcd63EXWJKAbYMFWsZjn1FbS9Y3GpoL0EPv0GMoat5p1NtKMSdYvIklcvET_86N7S9IqR5bPfW1r1RaENKemtVypXchIk5-UmXYxE9OOkwjZaEYf0UT2mSKNOONQGXhqRi0t0gGRrkiisgFPCxYdBQsLts3Nj4cCpVjFYX5EX6Y0Yqvsk7c_w-0wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1751785670:AAHgkTbvVzJwI8_2H7LAyIA5wDVy_sgRVOY")
BOT_NAME = getenv("BOT_NAME", "𝚁𝚎𝚖 𝙼𝚞𝚜𝚒𝚌")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "queengemoy_project")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9a0bfe8b4b6478c6979a4.png")
admins = {}
API_ID = int(getenv("API_ID", "7703315"))
API_HASH = getenv("API_HASH", "43118491ea08de184cbbcd11a93398ec")
BOT_USERNAME = getenv("BOT_USERNAME", "RemxMusic69_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RamxMusic69_bot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "fantaestheticgang")
PROJECT_NAME = getenv("PROJECT_NAME", "RemXMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/brut-ctrl/RemXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "AUDEEE-WKVNES-UGXHIX-QFDHIU-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
PMMSG = getenv("PMMSG", f"Hi there, This is a music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "712147852 1408440765 1944787421 1820831401 1945910995 1909021805 1605366945").split()))