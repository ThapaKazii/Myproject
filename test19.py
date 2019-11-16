# From a list separate the integers, stings  and floats elements into three different lists.

list=["bibek",44,'puri',288.8,'gaida',33,12.0,]
list2=[]
list3=[]
list4=[]
for x in list:
    if type(x)==int:
        list2.append(x)
    elif type(x)==float:
        list3.append(x)
    elif type(x)==str:
        list4.append(x)
    else:
        print("Sorry, Undetermined one..")
print(list2)
print(list3)
print(list4)