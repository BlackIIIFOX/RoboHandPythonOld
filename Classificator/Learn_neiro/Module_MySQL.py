import MySQLdb
from MySQLdb import Error

def connect(): #соединеие с БД
    try:
        print('Соединение с MySQL database...')
        conn=MySQLdb.connect(host='localhost',database='robo_hand',user='root',password='h8970102742',use_unicode=True, charset ='utf8')
        print("Соединение установлено")
        return conn
    except Error as e:
        print(e)
        exit()

def close_connect(conn):
    conn.close()
    print("Соедениение с БД закрыто")
