from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7041601837:AAEobyHVJLZIqPYJC6S0SY4sUnR_jipOGp0')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum {full_name} ")

@bot.message_handler(content_types=['text', 'photo', 'video', 'animation', 'sticker'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id, chat_id, message.message_id)

bot.polling()