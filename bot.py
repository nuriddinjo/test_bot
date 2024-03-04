# Aiogram
# pyTelegramBotApi

from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7162023744:AAGMSH_CgbbMuRN_DDvJHElgerOYTD8wGeQ')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum {full_name} ")


@bot.message_handler(commands=['text','photo','video', 'animation','stiker'])
def reaction_to_message(message: Message):
    chat_id = message.chat_id
    bot.copy_message(5754538843, chat_id, message)


bot.polling()