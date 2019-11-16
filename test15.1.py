length1=input("Enter the first side: ")
if length1.isnumeric() == False and length1==0:
    print("Sorry, wrong input:")
else:
    length2=input("Enter the second side: ")
    if  length2.isnumeric()==False and length2==0:
        print("Sorry, wrong input:")
    else:
        length3=input("Enter the third side: ")
        if length1.isnumeric()==False and length1==0:
            print("Sorry, wrong input:")
        else:
            length4=input("Enter the fourth side")
            if length4.isnumeric()==False and length4==0:
                print("Sorry, wrong input:")
            else:
                if length1==length2==length3==length4 :
                    print("It is a Square..")
                elif length2==length1 and length3==length4  or length1==length3 and length2==length4 :
                    print("It is a Rectangle..")
                else:
                    print("It is a quadrilateral..")