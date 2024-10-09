from file_manager import read_applications, write_application, write_all_applications
from utils import validate_date, format_applications
from datetime import datetime

# Add a new job application
def add_application(company, position, date_applied, status):
    if not date_applied:
        date_applied = datetime.today().strftime('%Y-%m-%d')  # Auto-add today's date if not provided

    new_application = [company, position, date_applied, status]
    write_application(new_application)

# View all job applications
def view_applications():
    applications = read_applications()
    if not applications:
        print("No job applications found.")
    else:
        format_applications(applications)

# Edit an application
def edit_application(company):
    applications = read_applications()
    found = False
    for app in applications:
        if app[0].lower() == company.lower():
            print(f"Current details for {company}: {app}")
            print("Leave blank to skip editing.")
            new_company = input("Enter new company name (or press Enter to keep unchanged): ")
            new_position = input("Enter new position (or press Enter to keep unchanged): ")
            new_date_applied = input("Enter new date (YYYY-MM-DD) (or press Enter to keep unchanged): ")
            new_status = input("Enter new status (or press Enter to keep unchanged): ")

            if new_company:
                app[0] = new_company
            if new_position:
                app[1] = new_position
            if new_date_applied and validate_date(new_date_applied):
                app[2] = new_date_applied
            if new_status:
                app[3] = new_status

            found = True
            break

    if found:
        write_all_applications(applications)
        print(f"Application for {company} updated successfully!")
    else:
        print(f"No application found for {company}.")

# Update the status of a job application
def update_status(company, new_status):
    applications = read_applications()
    updated = False

    for app in applications:
        if app[0].lower() == company.lower():
            app[3] = new_status
            updated = True
            break

    if updated:
        write_all_applications(applications)
        print(f"Status for {company} updated successfully!")
    else:
        print(f"No application found for {company}.")
