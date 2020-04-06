#coding=utf-8
from django.db import connection,models
from collections import namedtuple

class getdatanbysql(models.Manager):
    def querydata(self,sql):
        '''默认以字典的方式返回结果'''
        with connection.cursor() as cursor:
            cursor.execute(sql)
            desc=cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])

        return [nt_result(*row) for row in cursor.fetchall()]

    def getdata(self):
        sql = '''SELECT COUNT(e.event_id) as wqrs,e.event_id,e.name,e.status,e.address,e.start_time,g.sign
                            FROM sign_event e 
                            LEFT JOIN sign_guest g ON e.event_id = g.event_id  
                            WHERE g.sign='0' GROUP BY e.event_id'''
        result=self.querydata(sql)
        return result

if __name__ == '__main__':
    data=getdatanbysql().getdata()
    print(data)

