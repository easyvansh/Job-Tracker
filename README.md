
# **Job Tracker CLI Application**

A robust command-line interface (CLI) application designed to help you keep track of job applications. It allows you to add, edit, and manage job applications, customize application stages, and automatically log today's date unless specified.

## **Key Features**

- **Add Job Applications**: Automatically records the current date unless specified. You can also add a custom stage or select predefined stages such as *Accepted*, *Rejected*, *Waitlisted*.
- **Edit Applications**: Modify any field (company, position, date, or status) of an existing application.
- **Update Application Status**: Easily update the status of any application from predefined or custom stages.
- **View Applications**: Display all your job applications in a neatly formatted table.
- **User-Friendly CLI**: An intuitive command-line interface that guides you through every step, making it easy to manage your job applications.

## **Installation**

### **Prerequisites**

- Python 3.x
- No external libraries are required as the app uses Python’s standard library.

### **Clone the Repository**

```bash
git clone https://github.com/easyvansh/Job-Tracker.git
cd Job-Tracker
```

### **Initialize the Job Tracker**

Before running the app, ensure that the necessary CSV file is created. This is done automatically the first time you run the application.

```bash
python app.py
```

## **How to Use**

Upon running the application, you will be presented with a menu offering several options:

```text
Job Application Tracker - Menu
1. Add a new application
2. View all applications
3. Update application status
4. Edit an existing application
5. Exit
```

### **1. Add a New Application**

When you choose to add a new job application, the system will ask for details such as:

- **Company name**: The name of the company you're applying to.
- **Position**: The job position you're applying for.
- **Date Applied**: (Optional) If left blank, today’s date is automatically added.
- **Status**: You can select from predefined stages or create a custom one.

### **2. View All Applications**

This option will display a neatly formatted table of all your current job applications, including:

- Company name
- Job position
- Date applied
- Status (Accepted, Rejected, Waitlisted, or a custom status)

### **3. Update Application Status**

To update the status of a particular application, you can select it by company name and then change the status to:

- **Accepted**
- **Rejected**
- **Waitlisted**
- Or a custom stage you define.

### **4. Edit an Existing Application**

This allows you to modify any detail of an existing job application (company name, job position, date applied, or status). You will be able to keep existing values or update them as needed.

### **5. Exit**

You can exit the application at any time by selecting this option.


## **CSV File**

The application stores all job applications in a `job_tracker.csv` file. This file is automatically created when you first run the application. The format is as follows:

```csv
Company,Position,Date Applied,Status
```

### **Sample CSV Data**

```csv
Company,Position,Date Applied,Status
Google,Software Engineer,2024-10-01,Accepted
Amazon,Backend Developer,2024-09-28,Waitlisted
Facebook,Frontend Engineer,2024-09-15,Rejected
```


## **License**

This project is licensed under the MIT License - see the [LICENSE](https://github.com/easyvansh/Job-Tracker/blob/main/LICENSE) file for details.

