grade = input('Enter Grade Marks')

marks: int = int(grade)
# convert to int
# print(type(marks))

# elif else statement

if marks > 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
elif marks >= 30:
    print("E")
else:
    print("F")
