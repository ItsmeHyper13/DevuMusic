# Powered by @HYPER_AD13 | @Dk143gurjar
# Dear Pero ppls Plish Don't remove this line from here🌚

# Powered by @HYPER_AD13 | @Dk143gurjar
# Dear Pero ppls Plish Don't remove this line from here🌚

from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME,BOT_IMG)
from cache.stuffs.string import (t1, t2, t3, t4, t5)
from cache.stuffs.string2 import (button1, button2, button3, button4)

@bot.on_message(filters.command("start"))
def start_(bot, message):
    message.reply_photo(
        photo=BOT_IMG,
        caption=t1.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(button1)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    message.reply_photo(
        photo=BOT_IMG,
        caption=t2.format(message.from_user.mention, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(button2)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
        callback.answer('Open Help Menu')
        callback.edit_message_text(
            t2.format(callback.from_user.mention, SUPPORT_GROUP),
            reply_markup=InlineKeyboardMarkup(button2)
        )
    elif callback.data == "repo_k":
        callback.answer('Source Code Of DevuMusic By @ShiningOff', show_alert=True)                
        callback.edit_message_text(
            t5.format(callback.from_user.mention, BOT_NAME),
            reply_markup=InlineKeyboardMarkup(button3)
        )
    elif callback.data == "HOME": 
        callback.answer('Return To Home Menu!')                      
        callback.edit_message_text(
            t1.format(callback.from_user.mention, BOT_NAME, SUPPORT_GROUP),
            reply_markup=InlineKeyboardMarkup(button1)
        )
    elif callback.data == "basic_":
        callback.answer('Basic Command Menu!')      
        callback.edit_message_text(
            t3,
            reply_markup=InlineKeyboardMarkup(button4)
        )
    elif callback.data == "admin_cmd":
        callback.answer('Advance Command Menu!!')               
        callback.edit_message_text(
            t4,
            reply_markup=InlineKeyboardMarkup(button4)
        )
    elif callback.data == "close_":
        callback.answer('Menu Closed!!', show_alert=True)
        callback.message.delete()
