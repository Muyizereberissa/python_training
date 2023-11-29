

def add():
    num1 = float(input("enter1"))
    num2 = float(input("enter2"))
    print(num1 + num2)
    main()


def sub():
    num1 = float(input("enter1"))
    num2 = float(input("enter2"))
    print(num1 + num2)
    main()


def mult():
    num1 = int(input("enter1"))
    num2 = float(input("enter2"))
    print(num1 * num2)
    main()


def div():
    num1 = float(input("enter1"))
    num2 = float(input("enter2"))
    print(num1 / num2)
    main()


def main():
    print("1.add")
    print("2.sub")
    print("3.mult")
    print("4.div")
    print("1.exit")

    choice = input("enter choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        sub()
    elif choice == "3":
        mult()
    elif choice == "4":
        div()
    else:
        print("enter valid code: ")
        main()


main()
