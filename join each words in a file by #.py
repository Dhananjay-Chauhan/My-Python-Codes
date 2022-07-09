f=open("poli.txt","r")
l=" "
m=[]
while l:
    l=f.readlines()
    for i in l:
        m.append(i)
f.close()
for n in m:
    n=n.split()
    "#".join(n)
print(m)
print(n)
        
    

