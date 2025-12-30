from database import create_tables, add_student, view_students

def menu():
    print("\n===== OpenTrack Menu =====")
    print("1. Add Student")
    print("2. View Students")
    print("4. Exit")

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

        elif choice == "4":
            print("Exiting OpenTrack. Bye 👋")
            break

        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
