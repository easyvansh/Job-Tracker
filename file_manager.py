import csv
import os

CSV_FILE = 'job_tracker.csv'

# Ensure the CSV file exists
def initialize_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Company', 'Position', 'Date Applied', 'Status'])

# Read all job applications from the CSV file
def read_applications():
    applications = []
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        applications = list(reader)
    return applications

# Write a new application to the CSV file
def write_application(application):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(application)

# Update the applications in the CSV file
def write_all_applications(applications):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company', 'Position', 'Date Applied', 'Status'])  # Rewrite header
        writer.writerows(applications)
