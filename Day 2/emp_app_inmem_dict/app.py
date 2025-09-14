import repo_inmem_dict as repo
def menu():
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
        id = int(input('ID: '))
        name = input('Name: ')
        age = int(input('Age: '))
        salary = float(input('Salary: '))
        is_active = input('Is Active (y/n): ').upper() == 'Y'
        employee = {'ID':id, 'Name':name , 'Age':age, 'Salary':salary, 'Is Active':is_active}
        repo.create_employee(employee)
        print(f'Employee {name} created successfully')
    elif choice == 2:
        employees = repo.read_all_employees()
        if len(employees) == 0:
            print('No employees found')
        else:
            for emp in employees:
                print(emp)
    elif choice == 3:
        id = int(input('Enter Employee ID to search: '))
        employee = repo.read_by_id(id)
        if employee == None:
            print(f'Employee with ID {id} not found')
        else:
            print(f'Employee found: {employee}')
    elif choice == 4:
        id = int(input('Enter Employee ID to update: '))
        employee = repo.read_by_id(id)
        if employee == None:
            print(f'Employee with ID {id} not found')
        else:
            salary = float(input('Salary: '))
            new_employee = {'ID':employee['ID'], 'Name':employee['Name'], 'Age':employee['Age'], 'Salary':salary, 'Is Active':employee['Is Active']}
            repo.update(id, new_employee)
            print(f'Employee {employee["Name"]} updated successfully')
    elif choice == 5:
        id = int(input('Enter Employee ID to delete: '))
        if repo.delete_employee(id):
            print(f'Employee with ID {id} deleted successfully')
        else:
            print(f'Employee with ID {id} not found')
    elif choice == 6:
        print('Exiting the program')
        exit(0)
    else:
        print('Invalid choice, please try again')

def menus():
    while True:
        choice = menu()
        print('-----------------------------------')
menus()