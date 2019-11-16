# WAP to print multiplication table of a number entered by the user.

number=int(input("Enter any number.. "))
print("The multiplication table of %s :" % number)
for x in range(1,11):
    print("%s * %s = %s" %(number, x, number*x))


