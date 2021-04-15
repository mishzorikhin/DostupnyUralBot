import sqlite3
import telebot
import requests
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

bot = telebot.TeleBot("1757847078:AAF9MlsiRs3Z1ChLzLJfrxnaA4sIPjAOIk4")

""" 
    name        TEXT,
    description TEXT,
    latitude    DOUBLE,
    longitude   DOUBLE,
    article     TEXT,
    video       TEXT,
    images      TEXT
    """


def getCoordinates(usersId, pleaces):
    conn = sqlite3.connect('DUral.db')
    cur = conn.cursor()

    searchID = "SELECT * FROM places WHERE name='" + pleaces + "'"

    cur.execute(searchID)
    results = cur.fetchall()
    print(results)

    hints = telebot.types.ReplyKeyboardMarkup(True, False)

    pleacesName = morph.parse(results[0][0])[0]

    hint = 'расcкажи o '+ (pleacesName.inflect({'loct'})[0]).title()
    hints.row(hint)
    #hints.row('Расскажи про каменный город')
    bot.send_location(usersId, results[0][2], results[0][3], reply_markup=hints)


"""
nomn	именительный	Кто? Что?	  хомяк ест
gent	родительный 	Кого? Чего?	  у нас нет хомяка
datv	дательный	    Кому? Чему?	  сказать хомяку спасибо
accs	винительный	    Кого? Что?	  хомяк читает книгу
ablt	творительный	Кем? Чем?	  зерно съедено хомяком
loct	предложный	    О ком? О чём? хомяка несут в корзинке
"""
def getDescription(usersId, pleaces):

    conn = sqlite3.connect('DUral.db')
    cur = conn.cursor()

    searchID = "SELECT * FROM places WHERE name='" + pleaces + "'"

    cur.execute(searchID)
    results = cur.fetchall()
    #print(results)

    hints = telebot.types.ReplyKeyboardMarkup(True, False)

    pleacesName = morph.parse(results[0][0])[0]

    hint = 'Где находиться '+ (pleacesName.inflect({'nomn'})[0]).title()
    hints.row(hint)
    #hints.row('Расскажи про каменный город')

    #bot.send_location(usersId, results[0][2], results[0][3], reply_markup=hints)

    description = results[0][4]
    bot.send_photo(usersId, results[0][6], caption = description, reply_markup=hints )






