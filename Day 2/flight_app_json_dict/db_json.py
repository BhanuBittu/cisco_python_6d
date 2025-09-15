import json
import os

def read_from_file(file_name = 'db.json'):
   if not os.path.exists(file_name):
       flights = []
       return flights

   with open(file_name, 'r') as reader:
       flights = json.load(reader)
       return flights
   return None

def write_to_file(flights, file_name = 'db.json'):
    with open(file_name, 'w') as writer:
         json.dump(flights, writer)