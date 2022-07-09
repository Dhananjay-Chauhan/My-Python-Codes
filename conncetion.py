import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',database='dhananjay',port='3307',password='dj123')
x=conn.cursor()
s='insert into dj values(7,1290,'F',10)'
x.execute(s)
conn.commit()
