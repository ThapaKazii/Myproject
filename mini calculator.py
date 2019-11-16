""" A mini calculator project.. """

print("What type of calculator do you wanna use?? ")
print("A. Basic calculator ")
print("B. Financial calculator ")
# print("C. Scientific calculator ")

## Input as user defined.
input1 = input("\tSelect what type of operation you wanna use.. \tA\tB\t")  # C\tD\t\n")
# first_num = float(input("Enter the first one..   "))
# second_num = float(input("Enter the second one..  "))

if input1 == 'A':
    print("Please select the operation. ")
    print("\t1. Addition.")
    print("\t2. Subtraction.")
    print("\t3. Division.")
    print("\t4. Multiplication.")
    print("\t5. Calculation of powers.")
    print("\t6. Square roots.")
    print("\t7. Cube roots.")
    print("\t8. Modulus.\n")

    input2 = input("What type of operation do tou want to perform? \t1\t2\t3\t4\t5\t6\t7\t8\t\n")

    # first_num = float(input("Enter the first one..   "))
    # second_num = float(input("Enter the second one..  "))
    if input2 == '1':
        print("\tFor Addition operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False  == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == False or second_num.isalpha() == True:
                print("Sorry, you have entered string value..")
            else:
                add = (float(first_num) + float(second_num))
                print("\t", first_num, "+", second_num, "=", float(add))
    elif input2 == '2':
        print("\tFor Subtraction operation: \n")
        first_num = input("\tEnter the first one..   ")
        if first_num.isalpha() == True or first_num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isalpha() == True or second_num.isdigit() == False:
                print("Sorry, you have entered string value..")
            else:
                subtract = (float(first_num) - float(second_num))
        print("\t", first_num, "-", second_num, "=", float(subtract))
    elif input2 == '3':
        print("\tFor Division operation: \n")
        first_num = input("\tEnter the first one..   ")
        if first_num.isalpha() == True or first_num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isalpha() == True or second_num.isdigit() == False:
                print("Sorry, you have entered string value..")
            else:
                division = float(first_num / second_num)
        print("\t", first_num, "/", second_num, "=", division)
    elif input2 == '4':
        print("\tFor Multiplication operation: \n")
        first_num = input("\tEnter the first one..   ")
        if first_num.isalpha() == True or first_num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isalpha() == True or second_num.isdigit() == False:
                print("Sorry, you have entered string value..")
            else:
                multiply = float(first_num * second_num)
        print("\t", first_num, "*", second_num, "=", multiply)
    elif input2 == '5':
        print("\tFor Calculation of power form: \n")
        first_num = input("\tEnter the first one..   ")
        if first_num.isalpha() == True or first_num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isalpha() == True or second_num.isdigit() == False:
                print("Sorry, you have entered string value..")
            else:
                power = float(first_num.__pow__(second_num))
        print("\t", first_num, "^", second_num, "=", power)
    elif input2 == '6':
        print("\tFor Square root operation: \n")
        num = float(input("\tEnter the number..   "))
        if num.isalpha() == True or num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            sq_root = float((num.__pow__(0.5)))
        print("\tThe square root of %s is %s " % (num, sq_root))
    elif input2 == '7':
        print("\tFor Cube root operation: \n")
        num = float(input("\tEnter the number..   "))
        if num.isalpha() == True or num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            cube_root = float(num.__pow__(float(1 / 3)))
        print("\tThe cube root of %s is %s " % (num, cube_root))
    elif input2 == '8':
        print("\tFor Modulus operation: \n")
        first_num = input("\tEnter the first one..   ")
        if first_num.isalpha() == True or first_num.isdigit() == False:
            print("Sorry, you have entered string value..")
        else:
            second_num = input("\tEnter the second one..  ")
            if second_num.isalpha() == True or second_num.isdigit() == False:
                print("Sorry, you have entered string value..")
            else:
                mod = float(first_num.__mod__(second_num))
        print("\t", first_num, "%", second_num, "=", mod)
    else:
        print("\tYou have entered wrong format..Check again.. ")
elif input1 == 'B':
    print("Please select the operation. ")
    print("1. Simple Interest.")
    #print("2. Compound Interest.")
    print("2. Conversion.\n")

    input3 = input("What type of operation do you want to perform? \t1\t2\t\n ")
    if input3 == '1':
        print("\tFor Simple Interest: \n")
        principle = float(input("\tEnter the principle..   "))
        time = float(input("\tEnter the time..  "))
        rate = float(input("\tEnter the rate.. "))
        interest = float((principle * time * rate) / 100)
        print("\tThe required simple interest is: ", interest)
    elif input3 == '2':
        print("\tFor Conversion: \n")
        print("Select the operation.. ")
        print("1. AUS and NPR")
        print("2. AED and NPR")
        print("3. USD and NPR")
        print("4. INR and NPR")
        print("5. EUS and NPR\n")
        input4 = input("What type of conversion do you want?\t1\t2\t3\t4\t5\t6\t\n")
        if input4 == '1':
            print("\tA.AUS to NPR : \n")
            print("\tN.NPR to AUS\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of AUS to NPR : \n")
                aud = (input("\tEnter the Australian Dollar:\t"))
                if aud.isalpha()==True or aud.isdigit()==True :
                    print("Invalid input..")
                else:
                    npr = float(aud) * 78.3910
                    print("\tNepalese rupee:\t", float(npr))
            elif input5 == 'N':
                print("\t1.Conversion of NPR to AUD : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isalpha()==True or npr.isdigit()==True :
                    print("Invalid input..")
                else:
                    aud = float(npr) * (1 / 78.3910)
                print("\tAustralian Dollar:\t", float(aud))
            else:
                print("\tPlease enter your value properly.")
        else:
            print("\tPlease enter your value properly.")
    else:
        print("\tPlease enter your value properly.")
else:
    print("\tPlease enter your value properly.")
