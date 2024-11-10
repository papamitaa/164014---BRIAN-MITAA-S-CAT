class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name:{self.name}, ID:{self.employee_id}, Salary:{self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def display_employees(self):
        print(f"\nEmployees in {self.department_name} Department:")
        for emp in self.employees:
            emp.display_details()

#Employee 1's info
employee1 = Employee("Omondi Timon", "Employee 1", 50000)
department = Department("IT")
department.add_employee(employee1)
department.display_employees()
print(f"Total Salary Expenditure: {department.calculate_total_salary()}")
