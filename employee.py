import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        self._name = name  # Encapsulating attributes with underscores for privacy
        self._emp_id = emp_id
        self._title = title
        self._department = department
    
    def display_details(self):
        """Display employee details."""
        print(f"Name: {self._name}, ID: {self._emp_id}, Title: {self._title}, Department: {self._department}")
    
    def __str__(self):
        """String representation of employee."""
        return f"{self._name} - ID: {self._emp_id}"

class Department:
    def __init__(self, name):
        self._name = name
        self._employees = []
    
    def add_employee(self, employee):
        """Add employee to department."""
        self._employees.append(employee)
    
    def remove_employee(self, emp_id):
        """Remove employee from department."""
        for employee in self._employees:
            if employee._emp_id == emp_id:
                self._employees.remove(employee)
                print(f"Employee with ID {emp_id} removed from {self._name}")
                return
        print(f"No employee with ID {emp_id} found in {self._name}")
    
    def list_employees(self):
        """List all employees in department."""
        if self._employees:
            print(f"Employees in {self._name}:")
            for employee in self._employees:
                print(employee)
        else:
            print(f"No employees in {self._name}")

class Company:
    def __init__(self):
        self._departments = {}
    
    def add_department(self, department_name):
        """Add department to company."""
        if department_name not in self._departments:
            self._departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print(f"Department '{department_name}' already exists.")
    
    def remove_department(self, department_name):
        """Remove department from company."""
        if department_name in self._departments:
            del self._departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print(f"Department '{department_name}' does not exist.")
    
    def display_departments(self):
        """Display all departments in company."""
        if self._departments:
            print("List of Departments:")
            for department_name in self._departments:
                print(department_name)
        else:
            print("No departments found.")

    def save_company_data(self, filename):
        """Save company data to a file."""
        with open(filename, 'w') as file:
            for department_name, department in self._departments.items():
                department_data = {
                    'name': department._name,
                    'employees': [{
                        'name': emp._name,
                        'emp_id': emp._emp_id,
                        'title': emp._title
                    } for emp in department._employees]
                }
                json.dump(department_data, file)
                file.write('\n')

    def load_company_data(self, filename):
        """Load company data from a file."""
        with open(filename, 'r') as file:
            for line in file:
                department_data = json.loads(line)
                department_name = department_data['name']
                employees_data = department_data['employees']
                department = Department(department_name)
                for emp_data in employees_data:
                    employee = Employee(emp_data['name'], emp_data['emp_id'], emp_data['title'], department_name)
                    department.add_employee(employee)
                self._departments[department_name] = department

def print_menu():
    """Print menu options for user interaction."""
    print("Employee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in a Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. List Departments")
    print("7. Save Company Data")
    print("8. Load Company Data")
    print("9. Exit")

def main():
    """Main function to run the program."""
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")
            if department in company._departments:
                employee = Employee(name, emp_id, title, department)
                company._departments[department].add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{department}' does not exist. Please add the department first.")

        elif choice == '2':
            department = input("Enter department name: ")
            if department in company._departments:
                emp_id = input("Enter employee ID to remove: ")
                company._departments[department].remove_employee(emp_id)
            else:
                print(f"Department '{department}' does not exist.")

        elif choice == '3':
            department = input("Enter department name: ")
            if department in company._departments:
                company._departments[department].list_employees()
            else:
                print(f"Department '{department}' does not exist.")

        elif choice == '4':
            department_name = input("Enter new department name: ")
            company.add_department(department_name)

        elif choice == '5':
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)

        elif choice == '6':
            company.display_departments()

        elif choice == '7':
            filename = input("Enter filename to save: ")
            company.save_company_data(filename)
            print("Company data saved.")

        elif choice == '8':
            filename = input("Enter filename to load: ")
            company.load_company_data(filename)
            print("Company data loaded.")

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
