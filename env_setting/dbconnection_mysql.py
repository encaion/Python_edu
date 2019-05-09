# !pip install pymysql
import pymysql
conn = pymysql.connect(host = '123.123.123.123', 
                       user = 'id', 
                       password = 'password',
                       db = 'DB name')
curs = conn.cursor()
curs.execute("SELECT * FROM table")
rows = curs.fetchall()

