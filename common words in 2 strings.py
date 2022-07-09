n=input("enter the string 1::")
m=input("enter the string 2::")
z=n.split()
x=m.split()
for i in z:
    if i in x:
        print("common words ::",i)
    else:
        print("uncommon words ::",i)
