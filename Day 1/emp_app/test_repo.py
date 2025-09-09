# Testing the repo.py file
#from repo import create_employee, read_all_employees, read_by_id, update, delete_employee
import repo
employee = (101, 'bhanu', 22, 50000, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully')
print('After add:', repo.read_all_employees())

employee = (102, 'mahesh', 25, 60000, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully')
print('After add:', repo.read_all_employees()) 

employee = (103, 'suresh', 28, 70000, False)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully')
print('After add:', repo.read_all_employees())

#test read by id
employee = repo.read_by_id(102)
if employee == None:
    print(f'Employee not found')
else:
    print(f'Employee found: {employee}')

#test update
employee = repo.read_by_id(103)
if employee == None:
    print(f'Employee not found')
else:
    id, name, age, salary, is_active = employee
    salary += 20000
    new_employee = (id, name, age, salary, is_active)
    repo.update(103, new_employee)
    print(f'Employee {name} updated successfully')
    print('After update:', repo.read_all_employees())

#test delete
repo.delete_employee(102)
print(f'Employee 102 deleted successfully')
print('After delete:', repo.read_all_employees())

# Make as app
