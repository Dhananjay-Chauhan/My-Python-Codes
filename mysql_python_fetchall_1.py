import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',database='dhananjay',port='3307',password='dj123')
x=conn.cursor()
sql="insert into dj(roll,feepending,gender,class) values({},{},'{}',{}).format(7,2500,F,10)"
data=x.execute(sql)
d=x.fetchall()
a=x.rowcount
print(a)
