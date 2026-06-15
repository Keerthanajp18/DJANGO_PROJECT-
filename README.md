# Student Management System

A simple Student Management System developed using Django and PostgreSQL.

## Features

- Add New Student
- View Student Details
- Update Student Information
- Delete Student Records
- Display All Students in a Table
- Connected with PostgreSQL Database

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- CSS

## Project Structure

```
Django-project/
│
├── app1/
├── core/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Database

PostgreSQL is used as the backend database for storing student records.

Student fields:
- Student ID
- Student Name
- Email
- Course

## CRUD Operations Implemented

### Create
Add new student records through the registration form.

### Read
View all student records and individual student details.

### Update
Edit existing student information.

### Delete
Remove student records from the database.

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create a virtual environment

```bash
python -m venv myenv
```

3. Activate virtual environment

```bash
myenv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run migrations

```bash
python manage.py migrate
```

6. Start the server

```bash
python manage.py runserver
```

7. Open browser

```
http://127.0.0.1:8000/
```

## Screens

- Home Page
- Student Registration Form
- Student List
- View Student
- Edit Student
- Delete Student

## Author

Keerthana V K

## Academic Purpose

This project was developed as part of Django Web Development laboratory/practice work to understand CRUD operations and PostgreSQL database integration.
