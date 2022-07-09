import csv
with open("trex.csv","r") as f:    
    x=csv.reader(f)
    for i in x:
        print(i)

