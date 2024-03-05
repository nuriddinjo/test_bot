from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7041601837:AAEobyHVJLZIqPYJC6S0SY4sUnR_jipOGp0')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum {full_name} ")

@bot.message_handler(content_types=['text'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(-4152379773, chat_id, message.message_id)
    bot.send_message(-4152379773, f"Bu habar {message.from_user.full_name} dan")

@bot.message_handler(content_types=['photo'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(-4152379773, chat_id, message.message_id)
    bot.send_message(-4152379773, f"Bu habar {message.from_user.full_name} dan")

@bot.message_handler(content_types=['video'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(-4152379773, chat_id, message.message_id)
    bot.send_message(-4152379773, f"Bu habar {message.from_user.full_name} dan")

@bot.message_handler(content_types=['sticker'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(-4152379773, chat_id, message.message_id)
    bot.send_message(-4152379773, f"Bu habar {message.from_user.full_name} dan")


bot.polling()