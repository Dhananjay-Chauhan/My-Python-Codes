def count():
    f=open("poli.txt","r")
    strl=" "
    counter=0
    while strl:
        strl=f.readlines()
        for i in strl:
            i=i.split()
            for j in i:
                if j=="principle":
                    counter+=1
    print(counter)
count()
        
