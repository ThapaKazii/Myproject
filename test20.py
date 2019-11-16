# From a list ask the user the number he wants to remove from the list and then print the list.

list=["bibek",44,'puri',288.8,'gaida',33,12.0,]
num=input(print("Which one do you wanna pop?\t"))
for num in list:
    list.pop(num)
print("You have sucessfully popped  " ,num)
print(list)

        #not done yet