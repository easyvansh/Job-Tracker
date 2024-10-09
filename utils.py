from datetime import datetime

# Validate date format (YYYY-MM-DD)
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Format and print applications for display
def format_applications(applications):
    print(f"{'Company':<20} {'Position':<20} {'Date Applied':<15} {'Status':<10}")
    print('-' * 65)
    for app in applications:
        company, position, date_applied, status = app
        print(f"{company:<20} {position:<20} {date_applied:<15} {status:<10}")
