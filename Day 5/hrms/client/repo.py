import requests

BASE_URL = "http://127.0.0.1:5000"

def create_employee(employee):
    url = f"{BASE_URL}/employees"
    response = requests.post(url, json=employee)
    created_employee = response.json()
    return created_employee

def read_all_employee():
    url = f"{BASE_URL}/employees"
    response = requests.get(url)
    dict_employees = response.json()
    return dict_employees


def read_by_id(id):
    url = f"{BASE_URL}/employees/{id}"
    response = requests.get(url)
    employee_dict = response.json()
    return employee_dict

def update(id, employee):
    url = f"{BASE_URL}/employees/{id}"
    response = requests.put(url, json=employee)
    updated_employee = response.json()
    return updated_employee

def delete_employee(id):
    url = f"{BASE_URL}/employees/{id}"
    response = requests.delete(url)
    return response.json()
