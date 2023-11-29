
def ave(sum2):
    print(sum2/5)


def sums(numbers):
    sum2 = 0
    for number in numbers:
        sum2 = sum2 + number
    print(sum2)
    ave(sum2)


def main():
    numbers = []
    for i in range(5):
        num = float(input(f"enter subject{i+1}: "))
        numbers.append(num)
    sums(numbers)


main()
