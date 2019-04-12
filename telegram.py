import requests
import mysql.connector
from mysql.connector import MySQLConnection, Error
def query_with_fetchone():

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='puneethchanda',
                                       password='Jyothiraj_112')
        cursor = conn.cursor()
        cursor.execute("SELECT `Monday`FROM `tt` WHERE 1")

        rows = cursor.fetchall()
        
        for i in rows:
            a.append(i)
    
    except Error as k:
        print(k)
    return(a)

def telegram_bot_sendtext(bot_message):

    bot_token = '829818125:AAGtg8og4X7SIoRVA-baPMoI1-O0djppoe0'
    bot_chatID = '791346451'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)

    return response.json()

if __name__ == '__main__':
    a=[]
    query_with_fetchone()
    for j in range(len(a)):
        print(a[j])
