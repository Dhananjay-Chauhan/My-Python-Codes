
for  o in range(4):
    
    n=input("enter the string::")
    m=input("enter the substring::")
    l=n.split()

    z=0
    x=0
    for i in l:
        
        if i in l and i==m :
            z=z+1
        else:
            x+=1
    if len(l)==x:

        print("substring is not found")
    else:
        print("substring is found")
      
