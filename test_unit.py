import unittest
from employee import Employee, Department, Company

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        # Create instances of Employee, Department, and Company for testing
        self.emp1 = Employee("Halitha", "101", "Software Developer", "Software Engineer")
        self.emp2 = Employee("Kavya", "102", "UI/UX Designer", "Software Engineer")
        self.emp3 = Employee("Priya", "201", "Marketing Manager", "Marketing")
        self.emp4 = Employee("Nizam", "105", "UI/UX Designer", "Software Engineer")

        self.dept1 = Department("Software Engineer")
        self.dept2 = Department("Marketing")

        self.company = Company()

    def test_add_employee(self):
        # Add employees to departments and check if they are added successfully
        self.dept1.add_employee(self.emp1)
        self.assertIn(self.emp1, self.dept1._employees)

        self.dept2.add_employee(self.emp3)
        self.assertIn(self.emp3, self.dept2._employees)

    def test_remove_employee(self):
        # Add and then remove employees from departments and check if they are removed successfully
        self.dept1.add_employee(self.emp1)
        self.dept1.add_employee(self.emp2)
        
        self.dept1.remove_employee("101")
        self.assertNotIn(self.emp1, self.dept1._employees)

    def test_add_department(self):
        # Add departments and check if they are added successfully
        self.company.add_department("Finance")
        self.assertIn("Finance", self.company._departments)

    def test_remove_department(self):
        # Add and then remove departments and check if they are removed successfully
        self.company.add_department("Finance")
        self.assertIn("Finance", self.company._departments)

        self.company.remove_department("Finance")
        self.assertNotIn("Finance", self.company._departments)

if __name__ == "__main__":
    unittest.main()
