def average(sum2,num):
    print(sum2/num)


def summ(numbers,num):
    sum2 = 0
    for number in numbers:
        sum2 = sum2 + number
    print(sum2)
    average(sum2, num)


def main():
    numbers = []
    num = int(input("enter a number of subjects: "))
    for i in range(num):
        number = int(input(f"enter subject {i + 1}: "))
        numbers.append(number)
    summ(numbers,num)


main()
