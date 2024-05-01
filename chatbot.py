#    _____________ 
#   |             |
#   |  LilithBot  |  
#   |_____________|

import telebot
import time
from dbconect import conn

API_KEY = "past your ID"
bot = telebot.TeleBot(API_KEY)


def checkstart():
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
                if temperature >= 26:
                    print(temperature)
                    chat = f"Favor verificar servidor: {temperature}°C"
                    bot.send_message(chat_id='enter with your IDCHAT', text=chat)

            time.sleep(300)


getDB()
bot.polling()

