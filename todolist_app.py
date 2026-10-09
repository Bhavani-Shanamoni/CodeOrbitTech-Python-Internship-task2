tasks = []
# function for adding taks
def add_tasks():
    task = input("Enter your task to be added:")
    tasks.append(task)
    print("Task added successfully")

#function for viewing tasks
def view_tasks():
    for number, task in enumerate(tasks, start = 1):
        print(number, task)

#function for removing taks
def remove_tasks():
    task_number = int(input("Enter the task number to be deleted:"))
    index = task_number - 1 # since index in list starts from 0
    tasks.pop(index)
    print("Task removed successfully!")

#main function
def main():
    while(1):
        print("1. Add Tasks\n2. View Tasks\n3. Remove Task")
        choice = int(input("Enter your choice number:"))
        if choice == 1:
            add_tasks()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_tasks()
        elif choice > 3:
            print("Invalid choice")
        if (input("Do you want to continue? (y/n): ") == 'n'):
            break
#calling main function
if __name__ == "__main__":
    main()      
        
