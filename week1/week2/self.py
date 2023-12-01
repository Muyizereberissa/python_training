students = {}
sums = 0
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name :")
    marks = input("Enter name ,marks for 5 subjects [use space] as separator: ").split()
    if any(mark.isdigit() for mark in marks):
        students[name] = marks
    else:
        print("Please Use Digits Only!")


# find sum of student

nm = input("Enter student to find sum of student: ")
if nm in students:
    for mark in students[nm]:
        sums += int(mark)
    print(f"{nm}'s Total mark are => {sums}")
else:
    print('Student doesnt exist')