
def total_sum():
    sun = 0
    for i in range(1,5,1):
        sun = sun + i
    return sun


# print(total_sum())
def totals(num):
    fact = 1
    for i in range(num, 1, -1):
        print(i,end="*")
        fact = fact * i
    return fact


print(totals(num=int(input("enter a number: "))))
