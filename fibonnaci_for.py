n=int(input("Enter the number of terms:"))
a=0
b=1
print(a,b)
for i in range(0,n-2):
    
    c=a+b
    d=a
    a=b
    b=c
    print(c)
    
    
