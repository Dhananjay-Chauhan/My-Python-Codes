for i in range(10):
    a=int(input("enter the  number of your choice::"))
    
    i=0
    while a!=0:
        a=a/10
        a=int(a)
        i+=1
    print(i)
