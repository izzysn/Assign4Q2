#Import required items
import requests
import json
import mysql.connector
from config import USERNAME, PASSWORD, HOST

# Define Post request for new event entry
# POST REQUEST
new_event = {
        "event_id": 22,
        "event_name": "Acoustic Café Nights",
        "band_name": "Melodic Strings",
        "date": "2024-10-05",
        "time": "19:30",
        "venue": "Cozy Corner Café",
        "seats_available": 50,
        "remaining_seats": 50
}

headers = {'content-type': 'application/json'}
result = requests.post(
    'http://127.0.0.1:5000/events', headers=headers, data=json.dumps(new_event)
)
print(result.json())

# Check the response
if response.status_code == 200:
    print("Event added successfully:", response.json())
else:
    print("Failed to add event. Status code:", response.status_code)


# Connect python database
class DbConnectionError(Exception):
    pass

# Now check if the database has connected.
def _connect_to_db(db_name):
    print("yes")
    cnx = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

## Define functions to call all events
# EXAMPLE 1
def get_all_events():
    try:
        db_name = 'events_database'  # update as required
        db_connection = _connect_to_db(db_name)
        print("connected")
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM events """
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == '__main__':
    get_all_events()












