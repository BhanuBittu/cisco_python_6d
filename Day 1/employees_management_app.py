employees = []
employee = ('bhanu', 22, 50000, True)
employees.append(employee)
employee = ('mahesh', 25, 60000, True)
employees.append(employee)
employee = ('suresh', 28, 70000, False)
employees.append(employee)
print('after adding employees', employees)
i = 0
search = 'suresh'
index = -1
for emp in employees:
    if emp[0] == search:
        index = i
        break
    i += 1
if index == -1:
    print(f'Employee {search} not found')
else:
    search_employee = employees[index]
    print(f'Employee {search} found at index {index}')
    salary = float(input('Salary: '))
    employees[index] = (search_employee[0], search_employee[1], salary, search_employee[3])
print('after search and update',employees)
employee = ('ramesh', 30, 80000, True)
employees.append(employee)
print('after adding new employee', employees)
employees.pop()
print('after removing ramesh employee', employees)

position = 1
employees.pop(position)
print(f'after removing employee at position {position}', employees)