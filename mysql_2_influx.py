#!/usr/bin/python3

import pymysql
from influxdb import InfluxDBClient
import datetime


connect_mysql = pymysql.connect(host='mysql.localhost.com',
                             user=admin',
                             password='password',
                             db='circlepix')

connect_influxdb = InfluxDBClient(host='influx.circlepix.com',
                                  port=8086,
                                  username='admin',
                                  password='password',
                                  database='INFLUX')


cursor = connect_mysql.cursor()

status_214  = 'select count(StatusIDE) from ImportScriptQueue group by StatusIDE having StatusIDE = 214;'
cursor.execute(status_214)

cur_time = str(datetime.datetime.now().isoformat())

data = cursor.fetchone()
metric = data[0]
print(str(metric) + ", " + str(cur_time))

json_body = [{"measurement": "ImportScriptNumber",  
            "tags": {'ImportScriptQueue': 'StatusIDE'},  
            "time": cur_time, 
            "fields": {"214": metric}
             }]

connect_influxdb.write_points(json_body, protocol=u'json')
