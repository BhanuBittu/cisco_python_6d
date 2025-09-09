employees = []

def create_employee(employee):
    global employees
    employees.append(employee)

def read_all_employees():
    return employees

def read_by_id(id):
    for emp in employees:
        if emp[0] == id:
            return emp
    return None

def update(id, new_employee):
    i = 0
    for emp in employees:
        if emp[0] == id:
            employees[i] = new_employee
            break
        i += 1 

def delete_employee(id):
    index = -1
    i = 0
    for emp in employees:
        if emp[0] == id:
            index = i
            break
        i += 1
    if index != -1:
        employees.pop(index)
        return True
    return False
    
