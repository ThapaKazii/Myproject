""" A mini calculator project.. """

print("What type of calculator do you wanna use?? ")
print("A. Basic calculator ")
print("B. Financial calculator ")
# print("C. Scientific calculator ")
# print("D. Basic calculator\n")

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

    input2 = input("What type of operation do you want to perform? \t1\t2\t3\t4\t5\t6\t7\t8\n")

    # first_num = float(input("Enter the first one..   "))
    # second_num = float(input("Enter the second one..  "))
    if input2 == '1':
        print("\tFor Addition operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False :
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                add = (float(first_num) + float(second_num))
                print("\t", first_num, "+", second_num, "=", float(add))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")
    elif input2 == '2':
        print("\tFor Subtraction operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False :
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                subtract = (float(first_num) - float(second_num))
                print("\t", first_num, "-", second_num, "=", float(subtract))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")

    elif input2 == '3':
        print("\tFor Division operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False:
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                division = (float(first_num) / float(second_num))
                print("\t", first_num, "/", second_num, "=", float(division))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")

    elif input2 == '4':
        print("\tFor Multiplication operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False :
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                multiply = (float(first_num) * float(second_num))
                print("\t", first_num, "*", second_num, "=", float(multiply))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")
    elif input2 == '5':
        print("\tFor Calculation of power form: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False:
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                power = (float(first_num).__pow__(float(second_num)))
                print("\t", first_num, "^", second_num, "=", float(power))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")
    elif input2 == '6':
        print("\tFor Square root operation: \n")
        num = (input("\tEnter the first one..   "))
        if num.isnumeric() == True or num.isalpha() == False:
            sq_root = float(num).__pow__(0.5)
            print("\tThe square root of %s is %s " % (num, sq_root))
        else:
            print("Sorry, you have entered wrong value..")
    elif input2 == '7':
        print("\tFor Cube root operation: \n")
        num = (input("\tEnter the first one..   "))
        if num.isnumeric() == True or num.isalpha() == False :
            cube_root = float(num).__pow__(1 / 3)
            print("\tThe cube root of %s is %s " % (num, cube_root))
        else:
            print("Sorry, you have entered worng value..")
    elif input2 == '8':
        print("\tFor Modulus operation: \n")
        first_num = (input("\tEnter the first one..   "))
        if first_num.isnumeric() == True or first_num.isalpha() == False :
            second_num = input("\tEnter the second one..  ")
            if second_num.isnumeric() == True or second_num.isalpha() == False:
                mod = (float(first_num).__mod__(float(second_num)))
                print("\t", first_num, "%", second_num, "=", float(mod))
            else:
                print("Sorry, you have entered wrong value..")
        else:
            print("Sorry, you have entered wrong value..")
    else:
        print("\tYou have entered wrong format and enter again.. ")
elif input1 == 'B':
    print("Please select the operation. ")
    print("1. Simple Interest.")
    # print("2. Compound Interest.")
    print("2. Conversion.\n")

    input3 = input("What type of operation do you want to perform? \t1\t2\t\n ")
    if input3 == '1':
        print("\tFor Simple Interest: \n")
        principle = (input("\tEnter the principle..   "))
        if principle.isnumeric() == True or principle.isalpha() == False :
            time = (input("\tEnter the time..  "))
            if time.isnumeric() == True or time.isalpha() == False:
                rate = (input("\tEnter the rate.. "))
                if rate.isnumeric() == True or rate.isalpha() == False:
                    interest = ((float(principle) * float(time) * float(rate)) / 100)
                    print("\tThe required simple interest is: ", interest)
                else:
                    print("Sorry, Invalid Input..")
            else:
                print("Sorry, Invalid Input..")

                print("Sorry, Invalid Input..")
        else:
            print("Sorry, Invalid Input..")

    elif input3 == '2':
        print("\tFor Conversion: \n")
        print("Select the operation.. ")
        print("1. AUS and NPR")
        print("2. AED and NPR")
        print("3. USD and NPR")
        print("4. INR and NPR")
        print("5. EUS and NPR\n")
        input4 = input("What type of conversion do you want?\t1\t2\t3\t4\t5\t\n")
        if input4 == '1':
            print("\tA.AUD to NPR : \n")
            print("\tN.NPR to AUS\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of AUD to NPR : \n")
                aud = (input("\tEnter the Australian Dollar:\t"))
                if aud.isnumeric() == True or aud.isalpha() == False :
                    npr = float(aud) * 78.3910
                    print("\tNepalese rupee:\t", float(npr))
                else:
                    print("Invalid input..")

            elif input5 == 'N':
                print("\t1.Conversion of NPR to AUD : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isnumeric() == True or npr.isalpha() == False :
                    aud = float(npr) * (1 / 78.3910)
                    print("\tAustralian Dollar:\t", float(aud))
                else:
                    print("Invalid input..")
        elif input4 == '2':
            print("\tA.AED to NPR : \n")
            print("\tN.NPR to AED\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of AED to NPR : \n")
                uae = (input("\tEnter the UAE Dirham:\t"))
                if uae.isnumeric() == True or uae.isalpha() == False :
                    npr = float(uae) * 31.28
                    print("\tNepalese rupee:\t", float(npr))
                else:
                    print("Invalid input..")
            elif input5 == 'N':
                print("\t1.Conversion of NPR to AED : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isnumeric() == True or npr.isalpha() == False:
                    print("Invalid input..")
                else:
                    uae = float(npr) * (1 / 31.28)
                    print("\tUAE Dirham:\t", float(uae))
        elif input4 == '3':
            print("\tA.USD to NPR : \n")
            print("\tN.NPR to USD\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of USD to NPR : \n")
                usd = (input("\tEnter the United States Dollar:\t"))
                if usd.isnumeric() == True or usd.isalpha() == False:
                    print("Invalid input..")
                else:
                    npr = float(usd) * 114.90
                    print("\tNepalese rupee:\t", float(npr))
            elif input5 == 'N':
                print("\t1.Conversion of NPR to USD : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isnumeric() == True or npr.isalpha() == False:
                    print("Invalid input..")
                else:
                    usd = float(npr) * (1 / 114.90)
                    print("\tUnited State Dollar:\t", float(usd))
        elif input4 == '4':
            print("\tA.INR to NPR : \n")
            print("\tN.NPR to INR\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of INR to NPR : \n")
                inr = (input("\tEnter the Indian Rupee:\t"))
                if inr.isnumeric() == True or inr.isalpha() == False :
                    npr = float(inr) * 1.60
                    print("\tNepalese rupee:\t", float(npr))
                else:
                    print("Invalid input..")
            elif input5 == 'N':
                print("\t1.Conversion of NPR to INR : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isnumeric() == True or npr.isalpha() == False :
                    inr = float(npr) * (1 / 1.60)
                    print("\tIndian Rupee:\t", float(inr))
                else:
                    print("Invalid input..")

        if input4 == '5':
            print("\tA.EUS to NPR : \n")
            print("\tN.NPR to EUS\n")
            input5 = input("Which one do you want?\tA\tN\t")
            if input5 == 'A':
                print("\t1.Conversion of EUS to NPR : \n")
                eus = (input("\tEnter the European Dollar:\t"))
                if eus.isdigit() == True or eus.isalpha() == False :
                    npr = float(eus) * 126.98
                    print("\tNepalese rupee:\t", float(npr))
                else:
                    print("Invalid input..")`
            elif input5 == 'N':
                print("\t1.Conversion of NPR to EUS : \n")
                npr = (input("\tEnter the Nepalese Rupee:\t"))
                if npr.isnumeric() == True or npr.isalpha() == False:
                    eus = float(npr) * (1 / 126.98)
                    print("\tEuropean Dollar:\t", float(eus))
                else:
                    print("Invalid input..")



else:
    print("\tPlease enter your value properly.")
