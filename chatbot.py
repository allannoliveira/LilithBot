#    _____________ 
#   |             |
#   |  LilithBot  |  
#   |_____________|

import telebot
import time
from dbconect import conn

API_KEY = "7191570401:AAFY0QPJq3WNoBob-CHy60SZFxYrLg6N5tM"
bot = telebot.TeleBot(API_KEY)


def checkstart(message):
    return True



@bot.message_handler(func=checkstart)
def respond(message):
    bot.reply_to(message, "Hello, we are starting server temperature monitoring")


def getDB():
    connection = conn()
    if connection:
        cursor = connection.cursor()
        while True:
            cursor.execute("SELECT * FROM temp ORDER BY id DESC LIMIT 1")
            result = cursor.fetchone()

            if result: 
                temperature = float(result[1])
                if temperature >= 23:
                    print(temperature)
                    chat = f"Favor verificar servidor: {temperature}°C"
                    bot.send_message(chat_id='-1002063771313', text=chat)

            time.sleep(300)


getDB()
bot.polling()

