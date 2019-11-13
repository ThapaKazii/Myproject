
   # Take five marks input from the user and then input into the list and then print the sum of all marks


TOC=float(input("Enter the marks of TOC: "))
Maths=float(input("Enter the marks of Maths: "))
Programming=float(input("Enter the marks of Programming: "))
Statistics=float(input("Enter the marks of Statistics: "))
IT=float(input("Enter the marks of IT: "))

list=[TOC, Maths, Programming, Statistics, IT]
print(list)
total=int(sum(list))
print('The sum of all the subjects is: ',total)