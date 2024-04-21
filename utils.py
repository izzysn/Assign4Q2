# Define some useful fuctions
def search_event(eventID, events_list):
    return [eachevent for eachevent in events_list if eachevent["event_id"] == eventID]

def search_by_venue(venuepicked, events_list):
    return [eachvenue for eachvenue in events_list if eachvenue["venue"] == venuepicked]

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