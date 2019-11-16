#WAP that ask the user to enter name, age and mobile number with validation.
            #without loop
name = input("Enter your name:  ")
if name.isalpha()==False or len(name )< 3:
    print("Sorry, enter the name properly with characters and more than two digits.")
else:
    age=int(input("Enter your age: "))
    if age<19 :
        print("Your age must be more than 18")
    else:
        mob=(input("Enter your mobile number: "))
        if len(mob)!=10 or mob.isalpha():
            print("Your mobile number format is incorrect..")
        else:
            print("Your name is: ", name)
            print("Your age is: ", age)
            print("Your mobile number is: ", mob)

