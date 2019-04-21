import json 
import requests
import datetime
import server
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

TOKEN = "Token here"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_chat_id(updates,i):
    num_updates = len(updates["result"])
    chat_id = updates["result"][i]["message"]["chat"]["id"]
    return (chat_id)

def no_subscribers(updates):
    num_subs = len(updates["result"])
    return(num_subs)

def send_message(tt,chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(tt, chat_id)
    get_url(url)
    
if __name__ == '__main__':
    a=[]
    b=[]
    now = datetime.datetime.now()
    day=now.strftime("%A")
    query_with_fetchone(day)
    for i in range(no_subscribers(get_updates())):
        b.append(get_chat_id(get_updates(),i))
    for i in range(no_subscribers(get_updates())):
        for j in range(len(a)):
            tt=a[j][0]
            chat = b[i]
            send_message(tt, chat)
