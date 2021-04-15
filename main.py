import telebot
import sqlite3
import command
import decryptionText
import places

from telebot import types

bot = telebot.TeleBot("1757847078:AAF9MlsiRs3Z1ChLzLJfrxnaA4sIPjAOIk4")

newUser = True
hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def start_message(message):
    command.start(message)


@bot.message_handler(content_types=['text'])
def text_command(message):
    print(message.text)
    decryptionText.decryption(message, message.chat.id)

    # bot.send_message(message.chat.id,"Ok", reply_markup=hideBoard)

    # bot.send_photo(message.chat.id, 'https://uraloved.ru/images/mesta/perm-krai/hohlovka/hohlovka-11.jpg', caption="test")


"""@bot.message_handler(content_types=['location'])
def handle_loc(message):
    print(message.location)
    bot.send_location(message.chat.id, )"""

decryptionText.decryption()

if __name__ == "__main__":
    bot.polling()
