list=eval(input("enter a list:"))
m=0
l=len(list)
for a in range(l):
    d=len(list[a])
    if d>m:
        m=d
        
print("max:",list[a])
