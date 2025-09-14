import pickle
import os

def read_from_file(file_name = 'db.dat'):
   if not os.path.exists(file_name):
       employees = []
       return employees
   
   with open(file_name, 'rb') as reader:
       employees = pickle.load(reader)
       return employees
   return None

def write_to_file(employees, file_name = 'db.dat'):
    with open(file_name, 'wb') as writer:
        pickle.dump(employees, writer)
