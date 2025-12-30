from database import create_tables

def menu():
    print("\n1. Add Student")
    print("2. View Students")
    print("4. Exit")

def main():
    print("Welcome to OpenTrack!")
    create_tables()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "4":
            print("Exiting OpenTrack...")
            break

if __name__ == "__main__":
    main()
