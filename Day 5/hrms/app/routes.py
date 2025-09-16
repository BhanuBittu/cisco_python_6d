from datetime import timedelta
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import app.crud as crud 
from app.config import config
import app.mail as mail

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URL']
application.config['SQLALCHEMY_ECHO'] = True

crud.db.init_app(application)   #App to db configuration

# create the tables
with application.app_context():
    crud.db.create_all()

@application.route('/employees', methods=['POST'])
def create():
    employee_dict = request.json
    crud.create_employee(employee_dict)
    emp_id = employee_dict['id']
    savedEmployee_dict = crud.read_by_id(emp_id)
    #sending the mail
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    emp_id = employee_dict['id']
    name = employee_dict['name']
    age = employee_dict['age']
    salary = employee_dict['salary']
    is_active = 'Yes' if employee_dict['is_active'] else 'No'

    subject = f'{date_time_str} Employee {name} Created'
    mail_body = f"Employee Created Successfully with details: {savedEmployee_dict}"
    result = mail.send_gmail(mail.to_address, subject, mail_body)
    return jsonify(savedEmployee_dict)

@application.route('/employees', methods=['GET'])
def read_all():
    employees_dict = crud.read_all_employee()
    return jsonify(employees_dict)

@application.route('/employees/<id>', methods=['GET'])
def read_by_id(id):
    id = int(id)
    employee_dict = crud.read_by_id(id)
    if not employee_dict:
        return jsonify({'message': f'Employee with id {id} not found'}), 404
    return jsonify(employee_dict)

@application.route('/employees/<id>', methods=['PUT'])
def update(id):
    id = int(id)
    employee_dict = request.json
    crud.update(id, employee_dict)
    savedEmployee_dict = crud.read_by_id(id)
    return jsonify(savedEmployee_dict)

@application.route('/employees/<id>', methods=['DELETE'])
def delete(id):
    id = int(id)
    crud.delete_employee(id)
    return jsonify({'message': f'Employee with id {id} deleted successfully'}), 200

