from tracker import add_application, view_applications, update_status, edit_application
from file_manager import initialize_file

def display_menu():
    print("\nJob Application Tracker - Menu")
    print("1. Add a new application")
    print("2. View all applications")
    print("3. Update application status")
    print("4. Edit an existing application")
    print("5. Exit")
    print("-" * 40)

def add_custom_stage():
    default_stages = ["Accepted", "Rejected", "Waitlisted"]
    print("\nCurrent stages: ", default_stages)
    add_custom = input("Would you like to add a custom stage? (yes/no): ").strip().lower()

    if add_custom == "yes":
        custom_stage = input("Enter custom stage: ")
        if custom_stage:
            default_stages.append(custom_stage)
    return default_stages

def menu():
    initialize_file()  # Ensure CSV file exists
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            company = input("Enter company name: ")
            position = input("Enter job position: ")
            date_applied = input("Enter date applied (YYYY-MM-DD) or press Enter for today: ")
            stages = add_custom_stage()
            status = input(f"Enter status ({', '.join(stages)}): ")
            add_application(company, position, date_applied, status)

        elif choice == '2':
            view_applications()

        elif choice == '3':
            company = input("Enter company name to update status: ")
            stages = add_custom_stage()
            new_status = input(f"Enter new status ({', '.join(stages)}): ")
            update_status(company, new_status)

        elif choice == '4':
            company = input("Enter company name to edit: ")
            edit_application(company)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    menu()
