import mysql.connector
from secondtry import settings

MYSQL_HOSTS =settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD =settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB

cnx = mysql.connector.connect(user = MYSQL_USER,password = MYSQL_PASSWORD,host = MYSQL_HOSTS,database = MYSQL_DB)
cur = cnx.cursor(buffered = True)

class Sql:
    @classmethod
    def insert_dd_name(cls,title,address):
        sql = 'INSERT INTO content (`title`,`address`) VALUES(%(title)s ,%(address)s)'
        value ={
            'title':title,
            'address':address
        }
        cur.execute(sql,value)
        cnx.commit()

