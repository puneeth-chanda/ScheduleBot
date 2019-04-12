import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='puneethchanda',
                                       password='Jyothiraj_112')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)

if __name__ == '__main__':
    connect()
