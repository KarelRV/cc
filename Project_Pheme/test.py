import pymysql
import pymysql.cursors
import pandas as pd
from datetime import datetime
str(datetime.now())

# Connect to the database

created_at = str(datetime.now())
text = "Hello HEnk #wobawaba"
hashtag = "#wobawaba"
sentiment_cat = "positve"
sentiment_score = 1

connection = pymysql.connect(host='pheme.cenvzddeh7ne.eu-west-1.rds.amazonaws.com',
user='PhemeUES528',
password='^d+L6s_yc<_TC%6',
db='Pheme',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
	# Read a single recor
	sql = "insert into  tweets values(NULL,'{0}','{1}', '{2}', '{3}', '{4}')".format(created_at,hashtag,text,sentiment_cat,sentiment_score)
	cursor.execute(sql)
	connection.commit()
connection.close()

print("well done")