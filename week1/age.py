#year_one = int(input("Enter year of birth: "))
#year_two = int(input("Enter current year: "))
#if year_two - year_one >= 18:
    #print("you are eligible to vote")
#else:
    #print("you are not eligible to vote")

def eligibility(year1,year2):
    if year2 - year1 >= 18:
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")


#eligibility(year1=int(input("Enter year1: ")),year2=int(input("Enter year2:")))


def multiple_entry(*student_name):
    return student_name


number_of_students= int(input(f"enter number of students: "))
student_name = [input(f"Enter student name {i+1}:") for i in range(number_of_students)]
print(multiple_entry(*student_name))