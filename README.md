# Student Management System

A web-based Student Management System developed using Python and Django with MySQL database integration.

## Features

- Student registration and management
- Add, edit, and delete student records
- Upload student profile images and certificates
- Search students by name, email, and course
- Pagination for student records
- Dashboard with student and course summaries
- Form validation
- Responsive interface using Bootstrap

## Technologies Used

- Python
- Django
- MySQL
- HTML, CSS, Bootstrap
- JavaScript

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd student_management
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment in Windows:

   ```powershell
   .\venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a MySQL database named `student_db`.

7. Create a `.env` file in the project root and configure:

   ```env
   DB_NAME=student_db
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

8. Run migrations:

   ```bash
   python manage.py migrate
   ```

9. Start the development server:

   ```bash
   python manage.py runserver
   ```

10. Open `http://127.0.0.1:8000/` in your browser.
