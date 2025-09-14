# employee = [{'id':id, 'name':name, 'age':age, 'salary':salary}]
import db_pickle as db
#Employee app using pickle binary persisten storage(DB)
file_name = 'employees.dat'
employees = db.read_from_file(file_name)

def create_employee(employee):
    global employees
    employees.append(employee)
    db.write_to_file(employees, file_name)

def read_all_employees():
    global employees
    return employees

def read_by_id(id): 
    global employees
    for emp in employees:
        if emp['ID'] == id:
            return emp
    return None

def update(id, new_employee):
    i = 0
    for emp in employees:
        if emp['ID'] == id:
            employees[i] = new_employee
            db.write_to_file(employees, file_name)
            break
        i += 1 

def delete_employee(id):
    index = -1
    i = 0
    for emp in employees:
        if emp['ID'] == id:
            index = i   
            db.write_to_file(employees, file_name)
            break
        i += 1
    if index != -1:
        employees.pop(index)
        return True
    return False
    
