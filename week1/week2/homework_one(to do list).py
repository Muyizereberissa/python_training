
tasks = []


def add_task():
    task = input("enter task: (type letter b/B to return)")
    if task.lower() == "b":
        main()
    else:
        tasks.append(task)
        add_task()


def task_view():
    print("here are your tasks")
    for i,task in enumerate(tasks):
        print(f"task{i+1} => {task}")
    main()


def delete_task():
    task = input("enter task to be deleted: ")
    if task in tasks:
        tasks.remove(task)
    task_view()


def update_task():
    task = input("enter task you want to replace: (enter b/B to return)")
    if task.lower == "b":
        main()
    else:
        if task in tasks:
            new_task = input("enter new task: ")
            tasks[tasks.index(task)] = new_task
            task_view()


def main():
    print("1. add tasks ")
    print("2. view tasks")
    print("3. delete task")
    print("4. update task")
    print("5. exit")
    choice = input("enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        task_view()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        print("*******Thank you for your time**********")
    else:
        print("invalid choice ")


main()
