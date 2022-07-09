import csv
f=open("qwerty.csv","w")
s=csv.writer(f)
z=[]

while True:
    n=input("enter the name::")
    r=int(input("enter the rollno.")) 
    z.append(n)
    z.append(r)
    s.writerow(z)
    q=input("y,n")
    if q== "n":
        break

f=open("qwerty.csv","r")
s=csv.reader(f)
for  i in s:
    print(i)
    
f.close()
