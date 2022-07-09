for t in range(5):
    l=[]
    s=0
    m=[]
    p=a=int(input("enter the  number of your choice::"))    
    length=0
    while a!=0:
        b=int(a/10)
        b=b*10
        r=a-b
        l.append(r)
        a=a/10
        a=int(a)
        length+=1


    for  i in l:
        i=i**3
        m.append(i)
      
    for y in m:
        s+=y
       
    if p==s:
        print("arm")
    else:
        print("not")
