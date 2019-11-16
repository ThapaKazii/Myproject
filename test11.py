#write a program for grading the students bassed on the marks
#90 to 100--A
#70-90--B
#70-40--C
#Below 40-- fail

marks = float(input("Enter your obtained marks: "))
if marks >=90 and marks <= 100:
    print("Congrats, you have passed in grade 'A'")
elif marks >= 70 and marks < 90 :
    print("You have passed in grade 'B'")
elif marks >= 40 and marks <70:
    print("You have passed in grade 'C'")
elif marks <40 and marks >= 0:
    print("Sorry, you have failed")
else:
    print("Sorry, wrong input marks...Check again and try..")
 