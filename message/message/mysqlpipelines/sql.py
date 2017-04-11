import mysql.connector
from message import settings

MYSQL_HOSTS=settings.MYSQL_HOSTS
MYSQL_USER =settings.MYSQL_USER
MYSQL_PASSWORD=settings.MYSQL_PASSWORD
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER ,password =MYSQL_PASSWORD,host =MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:

    @classmethod
    def insert_message(cls,webname,province,title,href,time):
        sql = 'INSERT INTO message(`webname`,`province`,`title`,`href`,`time`) VALUES(%(webname)s,%(province)s,%(title)s,%(href)s,%(time)s)'
        value ={
            'webname': webname,
            'province': province,
            'title': title,
            'href': href,
            'time': time
        }
        cur.execute(sql,value)
        cnx.commit()

    @classmethod
    def select(cls,href):
        sql="SELECT EXISTS(SELECT 1 FROM message WHERE href=%(href)s)"
        value={
            'herf': href
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]