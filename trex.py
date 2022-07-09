import csv
f=open("trex.csv","r")
x=csv.reader(f)
while True:
    z=x.reader(f)
    for i in z:
        print(i)
f.close()
