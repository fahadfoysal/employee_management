# Employee Management System

A Django-based Employee Management System that allows you to manage employees, including adding, editing, deleting, and searching employees with advanced filtering options.

## Features

- Add, edit, delete employee records.
- Resize employee photos before storage to optimize loading time.
- Search employees by partial matches in names and emails.
- Sortable columns: Name, Email, Mobile, Date of Birth.
- Pagination for efficient data retrieval and display.
- Confirmation popup for deletion actions.

## Technologies Used

### Backend

- **Python**: 3.x
- **Django**: 4.x
- **Pillow**: (for image processing)
- **SQLite**: (default database for Django projects)

### Frontend

- **HTML**: Structure and content of the web pages.
- **CSS**: Styling for the web pages to improve aesthetics and user experience.
- **Bootstrap**: Frontend framework for responsive design and pre-styled components.
- **AJAX**:For partial page updates without reloading.
- **DataTables**:A library for dynamic table.


## Requirements

- **Python**: 3.x
- **Django**: 4.x
- **Pillow**: (for image processing)
- **SQLite**: (default database for Django projects)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fahadfoysal/employee_management.git
    cd employee-management-system
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file does not exist, you can create it by adding:

    ```plaintext
    Django==4.x
    Pillow==9.x
    ```

5. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application in your web browser:**

    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## URL Endpoints

- **Employee List Page:** `/employees/`
  - Displays a list of all employees with pagination, sorting, and search functionality.

- **Add Employee Page:** `/employees/add/`
  - Form to add a new employee, including fields for first name, last name, email, mobile, date of birth and photo.

- **Edit Employee Page:** `/employees/update/<pk>/`
  - Form to edit an existing employee's information.

- **Delete Employee Action:** `/employees/delete/<pk>/`
  - Action to delete an employee after confirmation.

- **Admin Dashboard:** `/admin/`
  - Django's built-in admin interface for managing models and data.

## Usage

1. **Add Employee:**
   - Go to the "Add Employee" page.
   - Fill in the employee details, including uploading a photo (image will be resized automatically).
   - Click "Submit" to save the employee data.

2. **Edit Employee:**
   - On the employee list page, click the "Edit" button next to the desired employee.
   - Update the necessary details and save changes.

3. **Delete Employee:**
   - On the employee list page, click the "Delete" button next to the desired employee.
   - Confirm the deletion by clicking "Yes" in the confirmation popup.

4. **Search Employees:**
   - Use the search bar to find employees by name or email. The search supports partial matches (e.g., searching for "John" will return "John Doe" and "Doe John").

5. **Sort and Paginate:**
   - Click on column headers to sort the employee list by name, email, mobile, or date of birth.
   - Use pagination controls to navigate through the pages.


For any inquiries or support, please contact [fahadfoysal16@gmail.com](mailto:fahadfoysal16@gmail.com).
