f=open("zaq.txt")
str1=" "
z=0
while str1:
    str1=f.readlines()
    print(str1)
    for  i in str1:
        if i[0]=="a":
            z=z+1
print("the no , od linbes thsz t sytart  wiht a ::",z)
