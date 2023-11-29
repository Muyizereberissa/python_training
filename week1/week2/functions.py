# function for even numbers
def even_numbers():
    for i in range(10):
        if i %2 == 0:
            print(i)


# even_numbers()


def odd_numbers():
    for i in range(10):
        if i & 1:
            print(i)


# odd_numbers()


def user_name(name):
    i = 1
    while i <= 5:
        print(name)
        i += 1


# user_name(input("enter yor name: ",))
def sum_nums(num1, num2,):
    sum = num1 + num2
    print("sum = ",sum)


# sum_nums(num1=int(input("enter num: ")), num2=float(input("enter num2: ")))

def user_sum(num1, num2):
    sums = num1 + num2
    return sums


# print("sum = ", user_sum(num1=float(input("enter num: ")), num2=float(input("enter num2: "))))

def next_numbers(num1):
    next3 = []
    for i in range(num1, num1+10, 1):
        next3.append(i)
    return next3


# print(next_numbers(int(input("enter num: "))))








