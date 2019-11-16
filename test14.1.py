# WAP that ask the user to enter name, age and mobile number with validation.

name = input("Enter your name:  ")
while name.isalpha() == False or len(name) < 3:
    print("Sorry, wrong input..")
    name = input("Enter your name:  ")
mob_num = input("Enter your phone number...")
while mob_num.isalpha()==True or len(mob_num)!=10 :
    print("Sorry, Enter your mobile number properly..")
    mob_num = input("Enter your phone number...")
age = input("Enter your age: ")
while age.isdigit()==False  or int(age)<19:
    print("Enter your age properly..  ")
    age = input("Enter your age: ")
print("Your name is: ", name)
print("Your mobile number is: ", mob_num)
print("Yur age is: ",age)


