import os
import logging
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="


Ek = Client(
    "Lyrics-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Ek.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Lyrics Search Bot. Send Me A Song Name, I Will Give You The Lyrics. ** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("💬 Update Channel", url = "https://t.me/m2botz"),InlineKeyboardButton("🗣 Support Group", url = "https://t.me/m2botzsupport")],[InlineKeyboardButton('About😎', callback_data='about'),InlineKeyboardButton('Help⚙', callback_data='help')],[InlineKeyboardButton("🧑‍💻Developer", url = "https://t.me/ask_admin01")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Ek.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me A Song Name, I Will Give Lyrics Of That Song. \nBot By @M2Botz "
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("💬 Update Channel", url = "https://telegram.me/m2botz"),InlineKeyboardButton("🗣 Support Group", url = "https://t.me/m2botzsupport")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Ek.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**🤖 Bot :**[Lyrics Search Bot](https://t.me/Lyrics_Search_M2Bot)\n\n**🧑‍💻 Developer :** [M2](https://t.me/ask_admin01)\n\n**💬 Update Channel :** [Click Here](https://t.me/m2botz)\n\n** 🗣 Support Group:** [Click Here](https://t.me/m2botzsupport) \n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@Ek.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song) 
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻Developer", url = "https://t.me/ask_admin01")], [InlineKeyboardButton("💬 Update Channel", url = "https://telegram.me/m2botz"),InlineKeyboardButton("🗣 Support Group", url = "https://t.me/m2botzsupport")]]))
        except requests.ConnectionError as exception:
        	await hy.delete()
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = "https://t.me/ask_admin01")], [InlineKeyboardButton("💬 Update Channel", url = "https://telegram.me/m2botz"),InlineKeyboardButton("🗣 Support Group", url = "https://t.me/m2botzsupport")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made With ❤️ By @M2Botz**'
        return text


Ek.run()
