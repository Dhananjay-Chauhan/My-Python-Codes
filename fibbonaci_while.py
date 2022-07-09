n=int(input("enter no. of terms :"))
a=0
b=1
f=[]
i=0
while i<n:
    c=a+b
    d=a
    a=b
    b=c
    f.append(c)
print(f)
