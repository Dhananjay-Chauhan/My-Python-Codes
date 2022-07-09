def reqw():
    i=0
    k=0
    f=open("zaq.txt","r")
    q=" "
    while q:
        q=f.readline()
        y=q.split()
        w=str(y[0])
        w=w[0]
        if w=="a":
            i+=1
            j=i
        else:
            k+=1
    print("the no. of lines is",j)
    

reqw()

