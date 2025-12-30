from database import (
    create_tables,
    add_student,
    view_students,
    add_task,
    view_tasks,
    mark_task_completed
)

def menu():
    print("\n===== OpenTrack Menu =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Task to Student")
    print("4. View Tasks of Student")
    print("5. Mark Task as Completed")
    print("6. Exit")


def main():
    print("Welcome to OpenTrack!")
    create_tables()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter student name: ")
            branch = input("Enter branch: ")
            add_student(name, branch)
            print("✅ Student added successfully")

        elif choice == "2":
            students = view_students()
            print("\n--- Students List ---")
            for s in students:
                print(f"ID: {s[0]}, Name: {s[1]}, Branch: {s[2]}")

        elif choice == "3":
            student_id = input("Enter student ID: ")
            task = input("Enter task description: ")
            add_task(student_id, task)
            print("✅ Task added successfully")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            tasks = view_tasks(student_id)
            print("\n--- Task List ---")
            for t in tasks:
                print(f"Task ID: {t[0]}, Task: {t[1]}, Status: {t[2]}")
        elif choice == "5":
            task_id = input("Enter Task ID to mark as completed: ")
            mark_task_completed(task_id)
            print("✅ Task marked as Completed")
        elif choice == "6":
            print("Exiting OpenTrack. Bye 👋")
            break

        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
