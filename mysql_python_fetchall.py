import mysql.connector as a
con=a.connect(host="localhost",user="root",password="dj123",port="3307", database="dhananjay")
sql='SELECT name FROM dhananjay'
c=con.cursor()
c.execute(sql)
d=c.fetchall()
for j in d:
    print(j)
