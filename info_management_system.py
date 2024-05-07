class InformationManager:
    def __init__(self):
        self.information = {}

    def add_information(self, key, value):
        self.information[key] = value

    def view_information(self, key):
        if key in self.information:
            print(f"Information for key '{key}': {self.information[key]}")
        else:
            print(f"Key '{key}' not found.")

    def delete_information(self, key):
        if key in self.information:
            del self.information[key]
            print(f"Deleted information for key '{key}'.")
        else:
            print(f"Key '{key}' not found.")

    def list_all_information(self):
        print("All Information:")
        for key, value in self.information.items():
            print(f"{key}: {value}")


def main():
    manager = InformationManager()

    while True:
        print("\nMenu:")
        print("1. Add information")
        print("2. View information")
        print("3. Delete information")
        print("4. List all information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter information: ")
            manager.add_information(key, value)
            print("Information added successfully.")
        elif choice == '2':
            key = input("Enter key to view information: ")
            manager.view_information(key)
        elif choice == '3':
            key = input("Enter key to delete information: ")
            manager.delete_information(key)
        elif choice == '4':
            manager.list_all_information()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
