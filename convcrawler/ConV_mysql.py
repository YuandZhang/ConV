
import pymysql



def getConnection():
    conn=pymysql.connect(host='127.0.0.1',user='root',passwd='password',db='mysql',port=3306)
    return conn

def create_table(conn):
    cursor=conn.cursor()
    sql = "create table ConVmodels(mid integer primary key auto_increment," \
          "name varchar(50),nowConfirm int,confirm int,suspect int,dead int , heal int)"
    cursor.execute(sql)

def insert_data(conn,name,nowConfirm,confirm,suspect,dead,heal):
    insert_sql="insert into conv_ConVmodels(name,nowConfirm,confirm,suspect,dead,heal) values (%s,%s,%s,%s,%s,%s)"
    cursor=conn.cursor()
    cursor.execute(insert_sql,(name,nowConfirm,confirm,suspect,dead,heal))
    conn.commit()
def select_data(conn):
    select_sql='select * from my_movies'
    cursor=conn.cursor()
    cursor.execute(select_sql)
    rows=cursor.fetchall()
    for row in rows:
        print(row[0],row[1],row[2],row[3])

def update_data(conn,name,nowConfirm,confirm,suspect,dead,heal):
    update_sql="update conv_ConVmodels set nowConfirm=%s,confirm=%s,suspect=%s,dead=%s,heal=%s where name=%s "
    cursor=conn.cursor()
    cursor.execute(update_sql,(nowConfirm,confirm,suspect,dead,heal,name))
    conn.commit()

def truncate_data(conn):
    truncate_sql="truncate table conv_ConVmodels"
    cursor = conn.cursor()
    cursor.execute(truncate_sql)
    conn.commit()
