
# Take a string from the user and then ask the user which strng needs to be counted
name = str(input("Enter the name: "))
string = input("Enter the string to be counted: ")
upper=string.upper()
lower=string.lower()
big=(name.count(upper))
small=name.count(lower)
total=big+small
print("The total number of %c is : " %string, total)