""" Flight Management System using JSON file as DB """
import sys
import repo_json_dict as repo
def create():
    """
    Create a new flight.
    """
    flight_id = int(input('ID: '))
    flight_number = input('Flight Number: ')
    airline = input('Airline: ')
    capacity = int(input('Capacity: '))
    price = int(input('Price: '))
    source = input('Source: ')
    destination = input('Destination: ')
    flight = {'ID': flight_id, 'Flight Number': flight_number, 'Airline': airline, 'Capacity': capacity,
              'Price': price, 'Source': source, 'Destination': destination}
    repo.create_flight(flight)
    print(f'Flight {flight_number} created successfully')

def read_all():
    """
    Read all flights.
    """
    flights = repo.read_all_flights()
    if len(flights) == 0:
        print('No flights found')
    else:
        for flight in flights:
            print(flight)

def read_by_flight_ID():
    """
    Read flight by ID.
    """
    flight_id = int(input('Enter Flight ID to search: '))
    flight = repo.read_by_id(flight_id)
    if flight is None:
        print(f'Flight with ID {flight_id} not found')
    else:
        print(f'Flight found: {flight}')

def menu():
    """
    Menu for Flight Management System.
    """
    message ='''
    '1. Create Flight'
    '2. Read All Flights'
    '3. Read Flight by ID'
    '4. Update Flight'
    '5. Delete Flight'
    '6. Exit' 
    Your choice: '''
    choice = int(input(message))
    if choice == 1:
        create()
    elif choice == 2:
        read_all()
    elif choice == 3:
        read_by_flight_ID()
    elif choice == 4:
        flight_id = int(input('Enter Flight ID to update: '))
        flight = repo.read_by_id(flight_id)
        if flight is None:
            print(f'Flight with ID {flight_id} not found')
        else:
            print(f'Current details: {flight}')
            flight_number = input('Flight Number: ')
            airline = input('Airline: ')
            capacity = int(input('Capacity: '))
            price = int(input('Price: '))
            source = input('Source: ')
            destination = input('Destination: ')
            updated_flight = {'ID': flight_id, 'Flight Number': flight_number, 'Airline': airline, 'Capacity': capacity,
                              'Price': price, 'Source': source, 'Destination': destination}
            repo.update_flight(updated_flight)
            print(f'Flight with ID {flight_id} updated successfully')
    elif choice == 5:
        flight_id = int(input('Enter Flight ID to delete: '))
        flight = repo.read_by_id(flight_id)
        if flight is None:
            print(f'Flight with ID {flight_id} not found')
        else:
            repo.delete_flight(flight_id)
            print(f'Flight with ID {flight_id} deleted successfully')
    elif choice == 6:
        print('Exiting...')
        sys.exit(0)
    else:
        print('Invalid choice, please try again.')

def main():
    """
    Main function to run the Flight Management System.
    """
    print('Welcome to the Flight Management System')
    while True:
        menu()

main()
