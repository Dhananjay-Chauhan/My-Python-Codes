def count():
    f=open("poli.txt","r")
    strl=" "
    counter=0
    while strl:
        strl=f.readlines()
        for i in strl:
            
            for j in i:
                if j=="a":
                    counter+=1
    print(counter)
count()
        
