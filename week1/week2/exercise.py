students = {}


def add_student():
    name = input("enter student name(press d to return): ")
    if name.lower() == "d":
        main()
    marks = input("enter student marks(press d to return): ")
    if marks.lower() == "d":
        main()
    else:
        students[name] = marks
    add_student()


def view_students():
    for name, marks in students.items():
        print(f"{name} => {marks}")
    main()


def search():
    name = input("enter student name you want: ")
    for name, marks in students.items():
        if name in students:
            print(name,"=>", students[name])
    main()


def main():
    print("1. add student name")
    print("2. view_students")
    print("3.search")
    print("4. exit")
    choice = input("enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search()
    elif choice == 4:
        exit()
    else:
        print("invalid choice try again!")


#main()


student_list = {}
student = int(input("enter number of students: "))
for i in range(student):
    name = input(f"enter name{i+1}: ")
    marks = (input("enter marks: ").split())
    student_list[name] = marks
    sums = sum(student_list.marks())
print(f"{student_list} => {sums}")


#def student_reg():
    #student = input("enter number of students:")
