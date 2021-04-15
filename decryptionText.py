import sqlite3
import telebot
import urllib.request
from urllib.request import urlopen
from io import BytesIO
import places

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

bot = telebot.TeleBot("1757847078:AAF9MlsiRs3Z1ChLzLJfrxnaA4sIPjAOIk4")


def decryption(message, chatID) :
    getNav = False
    aboutNav = False

    conn = sqlite3.connect('DUral.db')
    cur = conn.cursor()

    searchID = "SELECT name FROM places"

    cur.execute(searchID)
    results = cur.fetchall()

    namePlaces = []
    for name in results:
        namePlaces.append(name[0])

    string = message.text.split()
    characters = []

    for wordNoNorm in string:
        characters.append(morph.parse(wordNoNorm)[0].normal_form)

    for word in characters:

        if word == 'где' or word == 'находится' or word == 'пройти' or word == 'доехать' or word == 'добраться' or word == 'попасть' or word == 'как' or word == 'маршрут':
            getNav = True

        if word == 'расcказать' or word == 'о':
            aboutNav = True

        checkPleace = "SELECT name FROM places WHERE name='" + word + "'"

        cur.execute(checkPleace)
        results = cur.fetchall()
        # print(results)
        if results:
            # print(results[0][0])
            getPleace = results[0][0]

            if getNav:
                places.getCoordinates(chatID, getPleace)
                getNav = False

            if aboutNav:
                places.getDescription(chatID, getPleace)
                aboutNav = False

"""
        if word == 'футболка' or word == 'шапка' or word == 'футболка' or word == 'шапка' ::
            aboutNav = True"""



    #
    # places.getDescription(message.chat.id, 'Хохловка')
