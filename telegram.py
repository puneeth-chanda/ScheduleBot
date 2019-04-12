import requests
import datetime
from telegram.ext import ConversationHandler
import mysql.connector
from mysql.connector import MySQLConnection, Error
def query_with_fetchone(day):

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='puneethchanda',
                                       password='Jyothiraj_112')
        cursor = conn.cursor()
        if(day == 'Monday'):
            cursor.execute("SELECT Monday FROM `tt` WHERE 1")
        elif(day == 'Tuesday'):
            cursor.execute("SELECT Tuesday FROM `tt` WHERE 1")
        elif(day == 'Wednesday'):
            cursor.execute("SELECT Wednesday FROM `tt` WHERE 1")
        elif(day == 'Thursday'):
            cursor.execute("SELECT Thursday FROM `tt` WHERE 1")
        elif(day == 'Friday'):
            cursor.execute("SELECT Friday FROM `tt` WHERE 1")
        rows = cursor.fetchall()
        
        for i in rows:
            a.append(i)
    
    except Error as k:
        print(k)
    return(a)

def telegram_bot_sendtext(bot_message,bot_chatID):

    bot_token = '829818125:AAGtg8og4X7SIoRVA-baPMoI1-O0djppoe0'
    bot_chatID = '791346451'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)

    return response.json()

if __name__ == '__main__':
    a=[]
    now = datetime.datetime.now()
    day=now.strftime("%A")
    query_with_fetchone(day)
    bot_chatID = telegram.User.id
    for j in range(len(a)):
        tt=a[j][0]
        telegram_bot_sendtext(tt,bot_chatID)

