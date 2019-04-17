from mysql.connector import MySQLConnection, Error
import mysql.connector
def insert_book(chat_id):
    query = "insert into users(chat_id) values ('" + chat_id + "');"

    try:
        conn =  mysql.connector.connect(host = "localhost", database = "python_mysql", user="puneethchanda", password = "Jyothiraj_112")
 
        cursor = conn.cursor()
        cursor.execute(query)
 
        conn.commit()
    except Error as error:
        print(error)

 
def main():
   insert_book('9781436')
 
if __name__ == '__main__':
    main()
