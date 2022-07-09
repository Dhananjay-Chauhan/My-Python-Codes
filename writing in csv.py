import csv
f=open("trex.csv","w")
x=csv.writer(f,delimiter=',')
while True:
    n=input("enter the  name::")
    m=int(input("enter the roll. no.::"))
    b=input("enter the  class::")
    v=int(input("enter the  marks::"))
    z=[n,m,b,v]   
    x.writerow(z)
    choice=input("yes/no")
    if choice == "no":
        break
f.close()
