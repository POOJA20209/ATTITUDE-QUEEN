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
    
π | Telegraph Link:

    "https://telegra.ph/file/28267ea41e5379ffbaec2.jpg",
    "https://telegra.ph/file/bb2dd33c1dfdd1199a8dc.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Κα΄Κβ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nΙͺ α΄α΄  α΄α΄α΄Ιͺα΄α΄α΄α΄ - Η«α΄α΄α΄Ι΄ β**\nβββββββββββββββββββ\n\n"
  TEXT += f"Β» **α΄Κ α΄α΄α΄ α΄Κα΄α΄α΄Κβ : [βΈ’ α΄α΄α΄Ιͺα΄α΄α΄α΄ - Η«α΄α΄α΄Ι΄ βΈ₯](https://t.me/ATTITUDE_QUEEN_NO_1)** \n\n"
  TEXT += f"Β» **ΚΙͺΚΚα΄ΚΚ α΄ α΄ΚsΙͺα΄Ι΄ :** `{telever}` \n\n"
  TEXT += f"Β» **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄ :** `{tlhver}` \n\n"
  TEXT += f"Β» **α΄ΚΚα΄Ι’Κα΄α΄ α΄ α΄ΚsΙͺα΄Ι΄ :** `{pyrover}` \nβββββββββββββββββ\n\n"
  BUTTON = [
        [
            Button.url("Κα΄Κα΄β", f"https://t.me/Attitudequeenxrobot?start=help"),
            Button.url("sα΄α΄α΄α΄Κα΄β", f"https://t.me/Ourschennai"),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
