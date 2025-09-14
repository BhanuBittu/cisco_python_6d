import json
import os

def read_from_file(file_name = 'db.json'):
   if not os.path.exists(file_name):
       employees = []
       return employees

   with open(file_name, 'r') as reader:
       employees = json.load(reader)
       return employees
   return None

def write_to_file(employees, file_name = 'db.json'):
    with open(file_name, 'w') as writer:
        json.dump(employees, writer)
