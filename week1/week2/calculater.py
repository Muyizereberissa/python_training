def add(num1, num2):
    sign = input("enter sign: ")

    if sign == "+":
        print(num1 + num2)


def subtracted(num1, num2):
    sign = input("enter sign: ")
    print(num1 - num2)


def mult(num1, num2):
    sign = input("enter sign: ")
    if sign == "*":
        print(num1 * num2)


def division(num1, num2):
    sign = input("enter sign: ")
    if sign == "/":
        print(num1 / num2)


def modulo(num1, num2):
    sign = input("enter sign: ")
    if sign == "%":
        print(num1 % num2)


add(num1=(float(input("enter num: "))), num2=(float(input("enter num2: "))))
subtracted(num1=(float(input("enter num: "))), num2=(float(input("enter num2: "))))
mult(num1=(float(input("enter num: "))), num2=(float(input("enter num2: "))))
division(num1=(float(input("enter num: "))), num2=(float(input("enter num2: "))))
modulo(num1=(float(input("enter num: "))), num2=(float(input("enter num2: "))))
