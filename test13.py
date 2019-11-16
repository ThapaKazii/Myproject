#WAP to check whether the year is leap year or not.

year=int(input("Enter the year...."))
if year%4==0 and year%100==0 and year%400==0:
    print("%d is leap year " %year)
else:
    print("%d is not leap year " %year)