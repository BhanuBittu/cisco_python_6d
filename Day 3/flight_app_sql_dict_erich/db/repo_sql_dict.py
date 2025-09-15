from .db_setup import session, Flight
from .log import logging 
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import FlightNotFoundError, FlightAlreadyExistError, DatabaseError


def create_flight(flight):
    try:
        flight_id = Flight(flight_id = flight['id'],
            flight_number = flight['flight_number'],
            airline = flight['airline'],
            capacity = flight['capacity'],
            price = flight['price'],
            source = flight['source'],
            destination = flight['destination'] )
        session.add(flight_id) #INSERT stmt db 
        session.commit() 
        logging.info("flight created.")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate flight id:%s",ex)
        raise FlightAlreadyExistError(f"Flight id={flight['id']} exists already.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating flight:%s",ex)
        raise DatabaseError("Error in creating flight.")

def read_all_flights():
    flights = session.query(Flight).all()
    dict_flights = []
    for flight in flights:
        flight_dict = {'id':flight.id,
            'flight_number':flight.flight_number,
            'airline':flight.airline,
            'capacity':flight.capacity,
            'price':flight.price,
            'source':flight.source,
            'destination':flight.destination}
        dict_flights.append(flight_dict)
    logging.info("read all flights.")
    return dict_flights
def read_model_by_id(id):
    flight = session.query(Flight).filter_by(id = id).first()
    logging.info("read flight model.")
    return flight

def read_by_id(id):
    flight = read_model_by_id(id)
    if not flight: #if flight == None:
        logging.info(f"flight not found {id}.")
        return None
    flight_dict = {'id':flight.id,
        'flight_number':flight.flight_number,
        'airline':flight.airline,
        'capacity':flight.capacity,
        'price':flight.price,
        'source':flight.source,
        'destination':flight.destination}
    logging.info("read flight for given id.")
    return flight_dict

def update(id, new_flight):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return
    flight.flight_number = new_flight['flight_number']
    flight.airline = new_flight['airline']
    flight.capacity = new_flight['capacity']
    flight.price = new_flight['price']
    flight.source = new_flight['source']
    flight.destination = new_flight['destination']
    session.commit()
    logging.info("flight updated.")

def delete_flight(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return
    session.delete(flight)
    session.commit()
    logging.info("flight deleted.")


