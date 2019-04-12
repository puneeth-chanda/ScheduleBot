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
        a=[]
        for i in rows:
            a.append(i)
        for l in range(len(a)):
            print(a[l])
            
    except Error as k:
        print(k)

if __name__ == '__main__':

    query_with_fetchone()
