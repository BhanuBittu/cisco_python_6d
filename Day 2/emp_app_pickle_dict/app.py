"""
Employee Management System using Pickle and Dictionary
"""
import sys
import repo_pickle_dict as repo
def create():
    """
    Create a new employee.
    """
    emp_id = int(input('ID: '))
    name = input('Name: ')
    age = int(input('Age: '))
    salary = float(input('Salary: '))
    is_active = input('Is Active (y/n): ').upper() == 'Y'
    employee = {'ID':emp_id, 'Name':name , 'Age':age,
                     'Salary':salary, 'Is Active':is_active}
    repo.create_employee(employee)
    print(f'Employee {name} created successfully')

def read_all():
    """
    Read all employees.
    """
    employees = repo.read_all_employees()
    if len(employees) == 0:
        print('No employees found')
    else:
        for emp in employees:
            print(emp)

def read_by_id():
    """
    Read employee by ID.
    """
    emp_id = int(input('Enter Employee ID to search: '))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print(f'Employee with ID {emp_id} not found')
    else:
        print(f'Employee found: {employee}')

def update():
    """
    Update employee by ID.
    """
    emp_id = int(input('Enter Employee ID to update: '))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print(f'Employee with ID {emp_id} not found')
    else:
        salary = float(input('Salary: '))
        new_employee = {'ID':employee['ID'], 'Name':employee['Name'],
                        'Age':employee['Age'], 'Salary':salary, 'Is Active':employee['Is Active']}
        repo.update(emp_id, new_employee)
        print(f'Employee {employee["Name"]} updated successfully')

def menu():
    """
    Menu for Employee Management System.
    """
    message ='''
    '1. Create Employee'
    '2. Read All Employees'
    '3. Read Employee by ID'
    '4. Update Employee'
    '5. Delete Employee'
    '6. Exit' 
    Your choice: '''
    choice = int(input(message))
    if choice == 1:
        create()
    elif choice == 2:
        read_all()
    elif choice == 3:
        read_by_id()
    elif choice == 4:
        update()
    elif choice == 5:
        emp_id = int(input('Enter Employee ID to delete: '))
        if repo.delete_employee(emp_id):
            print(f'Employee with ID {emp_id} deleted successfully')
        else:
            print(f'Employee with ID {emp_id} not found')
    elif choice == 6:
        print('Exiting the program')
        sys.exit(0)
    else:
        print('Invalid choice, please try again')

def run_menu():
    """
    Loop the menu until user exits.
    """
    while True:
        menu()
        print('-' * 34,'\n')
run_menu()
