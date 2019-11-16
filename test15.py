 #WAP to enter the length of sides of a ploygon and find which polygon is it.

length1=int(input("Enter the first side: "))
length2=int(input("Enter the second side: "))
length3=int(input("Enter the third side: "))
length4=int(input("Enter the fourth side"))
if length1==length2==length3==length4 :
    print("It is a Square..")
elif length2==length1 and length3==length4  or length1==length3 and length2==length4 :
    print("It is a Rectangle..")
#elif length3==length1 and length2==length4  or length1==length4 and length2==length3 :
    #print("It is  a Kite..")
else:
    print("It is a quadrilateral..")