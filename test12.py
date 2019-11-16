#WAP to check whether the given number is odd or even.

number=int(input("Enter a number: "))
if number==0:
    print("You have entered Zero..Please input other positive numbers greater than Zero....")
elif number%2==0 :
    print("Even number..")
elif number<=0:
    print("You have entered negative numbers..Please input positive numbers..")
else:
    print("Odd number")