import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "[Forwarded from 📸 𝄪 ᴍɪʀᴀᴄʟᴇ ꭗ ɪᴍɢ 𝄪 📸]
🌐 | Telegraph Link:

    "https://telegra.ph/file/28267ea41e5379ffbaec2.jpg",
    "https://telegra.ph/file/bb2dd33c1dfdd1199a8dc.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ  ᴀᴛᴛɪᴛᴜᴅᴇ - ǫᴜᴇᴇɴ ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [⸢ ᴀᴛᴛɪᴛᴜᴅᴇ - ǫᴜᴇᴇɴ ⸥](https://t.me/ATTITUDE_QUEEN_NO_1)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/ "),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
