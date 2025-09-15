import db_json as db
#Flight app using json file persisten storage(DB)
file_name = 'flights.json'
flights = db.read_from_file(file_name)

def create_flight(flight):
    global flights
    flights.append(flight)
    db.write_to_file(flights, file_name)

def read_all_flights():
    global flights
    return flights

def read_by_id(id): 
    global flights
    for flight in flights:
        if flight['ID'] == id:
            return flight
    return None

def update_flight(id, new_flight):
    i = 0
    for flight in flights:
        if flight['ID'] == id:
            flights[i] = new_flight
            db.write_to_file(flights, file_name)
            break
        i += 1

def delete_flight(id):
    index = -1
    i = 0
    for flight in flights:
        if flight['ID'] == id:
            index = i   
            db.write_to_file(flights, file_name)
            break
        i += 1
    if index != -1:
        flights.pop(index)
        return True
    return False

