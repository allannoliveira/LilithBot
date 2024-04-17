#    _____________ 
#   |             |
#   |  LilithBot  |  
#   |_____________|

import telebot
import mysql.connector
import time

config = {
    'user': 'tester',
    'password': 'admin@123',
    'host': 'localhost',
    'port': 3306,  # Porta padrão do MySQL
    'database': 'dbmonitoramento',
    'raise_on_warnings': True
}

API_KEY = "7191570401:AAFY0QPJq3WNoBob-CHy60SZFxYrLg6N5tM"

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    bot = telebot.TeleBot(API_KEY)


    def checkstart(message):
        if message.text == "start":
            return True
        else:
            return False


    @bot.message_handler(func=checkstart)
    def respond(message):
        bot.reply_to(message, "Hello, we are starting server temperature monitoring")


    def getDB():
        while True:
            cursor.execute("SELECT * FROM impressoras")

            results = cursor.fetchall()

            for row in results:  # Alterei o nome da variável para 'row' para evitar confusão
                # Construa a mensagem a ser enviada para o bot
                mensagem = f"ID: {row[0]}, Nome: {row[1]}, Status: {row[2]}"  # Modifique conforme sua estrutura de dados
                bot.send_message(chat_id='SEU_CHAT_ID',
                                 text=mensagem)  # Substitua 'SEU_CHAT_ID' pelo ID do seu chat do Telegram

            time.sleep(300)


    getDB()
    bot.polling()
except mysql.connector.Error as error:
    print(f"Erro ao conectar ao banco de dados: {error}")
