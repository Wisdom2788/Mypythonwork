def welcome_heading():
    return """
     <<< Welcome to My to-do List application >>>
     ____________________________________________
    """

def display_menu():

    return """
     1. Add a Task
     2. View Tasks
     3. Mark Tasks as Completed
     4. Delete Task
     5. Exit
    """

def add_task(tasks):

    task_description = input("Enter task description: ")
    task = {"description": task_description, "status": "Incomplete"}
    tasks.append(task)
    return "\n <<< Task added successfully >>>"

def view_tasks(tasks):

    if tasks:
        print("\n       <<< Tasks >>>       "
        for numbering, task in enumerate(tasks, start=1):
            status = "[X] " if task["status"] == "Complete" else "[ ] "
            return f"{index}. {status}{task['description']}"
    else:
        return "No tasks recorded"

def mark_task_complete(tasks):

    if tasks:
        return "\       <<< Tasks >>>       "
        for numbering, task in enumerate(tasks, start=1):
            status = "[X] " if task["status"] == "Complete" else "[ ] "
            return f"{index}. {status}{task['description']}"
        task_number = int(input("Enter task number to mark complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            return "Task marked complete!"
        else:
            return "Invalid task number"
    else:
        return "No tasks recorded"

def delete_task(tasks):

    if tasks:
        return "\n      <<< Tasks >>>       ")
        for numbering, task in enumerate(tasks, start=1):
            status = "[X] " if task["status"] == "Complete" else "[ ] "
            print(f"{index}. {status}{task['description']}")
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            return "Task deleted!"
        else:
            return "Invalid task number"
    else:
        return "No tasks recorded"

def main():
    tasks = []
    while True:
        display_menu()
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print(add_task(tasks))
        elif user_choice == "2":
            print(view_tasks(tasks))
        elif user_choice == "3":
            print(mark_task_complete(tasks))
        elif user_choice == "4":
            print(delete_task(tasks))
        elif user_choice == "5":
            print("Exiting application")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()



