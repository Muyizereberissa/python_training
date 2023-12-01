
def register():
    names = input("enter name of registrars: ")
    user_age = input("enter user_age: ")
    qualities = input("enter a person's qualities")



def main():
    print("1. register exists")
    choice = input("enter choice: ")
    if choice == "1":
        register()


#main()
num = float(input("enter a number: "))
squares = {x: x**2 for x in range(int(num))}
print(squares)