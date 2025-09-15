import pytest 
from db import db_setup
from db import repo_sql_dict as repo

@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)
    #
    db_setup.Base.metadata.create_all(db_setup.engine)
    yield 
    db_setup.Base.metadata.drop_all(db_setup.engine)

def test_create_flight():
    flight = {'id':110,'flight_number':'AI202','airline':'Air India','capacity':180,'price':15000,'source':'Delhi','destination':'Mumbai'}
    repo.create_flight(flight)
    #
    savedFlight = repo.read_by_id(110)
    assert (savedFlight != None)
    assert (savedFlight['id'] == 110)
    assert (savedFlight['flight_number'] == 'AI202')
    assert (savedFlight['airline'] == 'Air India')
    assert (savedFlight['capacity'] == 180)
    assert (savedFlight['price'] == 15000)
    assert (savedFlight['source'] == 'Delhi')
    assert (savedFlight['destination'] == 'Mumbai')