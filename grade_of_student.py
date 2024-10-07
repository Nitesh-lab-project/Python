# Write a program to print the grade of student on the basis of marks obtained

marks=int(input("Enter Marks of Student:"))

if(marks>=90):
    Grade="A"
elif(marks<90 and marks>=80):
    Grade="B"
elif(marks<80 and marks>=70):
    Grade="C"
else:
    Grade="D"

print("Grade of student->",Grade)
