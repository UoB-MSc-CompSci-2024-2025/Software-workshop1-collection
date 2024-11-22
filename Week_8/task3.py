# You have been given the uncompleted code below for an HR
# system that includes payroll functionality. Your task is to
# complete the classes by including the necessary class
# attributes.
# First, you need to analyse the process_payroll function
# located at the bottom of the code below. From that code, you
# need to determine the attributes that each class must contain.
# After a bit of thinking, you have determined that these
# attributes are shared by all instances of the classes, hence
# they should be class attribute. Please assign realistic values
# to these attributes.
# Note: Within the process_payroll function, class attributes
# are accessed using the syntax.

class HRManager:
    # Add the class attributes
    def __init__(self, name, age, department, phone,annual_salary):
        self.name = name
        self.age = age
        self.department = department
        self.phone = phone
        self.annual_salary = annual_salary


class Employee:
    # Add the class attributes
    def __init__(self, name, age, address, phone, department, annual_salary):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.department = department
        self.annual_salary = annual_salary


# Program
# ==================================================================
# Function that prints the monthly salary of each employee
# and the total payroll expense for the company
def process_payroll(employees):
    total_payroll_expense = 0
    print("\n========= Welcome to the HR Payroll System =========\n")
    # Iterate over the list of instances to calculate
    # and display the monthly salary for each employee,
    # and add the total payroll expense
    for emp in employees:
        monthly_salary = emp.annual_salary / 12
        print(f"{emp.name.capitalize()}'s monthly salary is:${monthly_salary:.2f}")
        total_payroll_expense += monthly_salary
        # Print the total payroll expense for the month
    print("\nThe total payroll expense for the month is: $", total_payroll_expense)


employeeList = [
    Employee(name="Logesh sharma", age=28, address="B15 3SS", phone="8608922177", annual_salary=50000, department="CS"),
    HRManager(name="Nisha", age=49, phone="43534534", annual_salary=34523, department="HR")]

process_payroll(employeeList)
