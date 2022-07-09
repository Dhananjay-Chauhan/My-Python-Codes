a= input("enter a number : ")
h=[]
for i in  range(0,len(a)):
    b=int(a[i])
    h.append(b)
print(h)
l=[]
for j in range (0,len(h)):
    c=h[j]**3
    l.append(c)
print(l)
n=0
for k in range(0,len(l)):
    n=n+l[k]
print(n)
if int(a)==n:
    print("aarmstrong")
else:
    print("not armstrong")
