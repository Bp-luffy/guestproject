#coding=utf-8
from pymysql import cursors,connect

#连接数据库
conn=connect(host='47.101.169.25',
             user='pengl',
             password='pengl',
             db='testforpl',
             charset='utf8mb4',
             cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        #创建嘉宾数据
        sql='Insert Into sign_guest(realname,phone,email,sign,event_id,create_time) ' \
            'values ("tom",18883282817,"tom@mail.com",0,1,NOW());'
        cursor.execute(sql)
        conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "SELECT realname,phone,email,sign from sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18883281111',))
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()