def count(list1):
    count1=0
    count2=0
    neutral=0
    for i in list1:
        if i>0:
            count1=count1+1
        elif i<0:
            count2=count2+1
        else:
            neutral=neutral+1
    print("the no. of +ve numbers in the list are ::",count1)
    print("the no. of -ve numbers in the list are ::",count2)
    print("the no. of zeros in the list are ::",neutral)
list2=eval(input("enter list::"))
count(list2)
