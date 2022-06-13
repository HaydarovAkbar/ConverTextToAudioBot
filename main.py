"""
Tavsif: Textni Audio ko'rinishga o'tkazib beradigan bot Yozamiz!
Dasturchi: Haydarov Akbar
Sana: 2021/05/24 16:33
"""

from telegram.ext import Updater,CommandHandler
from telegram.ext import MessageHandler,Filters
from BOTmethods import *

Token = "1980376928:AAHYegmPVids6KxaKad7cK6cQfs9qyQZNUI"

updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
text_handler = MessageHandler(Filters.text,main)
photo_handler = MessageHandler(Filters.photo,photo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(photo_handler)

updater.start_polling()
print("Bot ishladi")
