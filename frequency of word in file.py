f=open("qaz.txt")
str1=" "
z=0
p=0
while str1:
    str1=f.readline()
    b=str1.split()
    c=len(b)
    p=p+c
    for i in b:
        if i=="computer":
            z=z+1
print("the no. of times the word computer appears is::",z)
print("the no. of times the word  appears is::",p)
