# Isabelle Shaw Nelson Assignment 4, Question 2
# This file defines the API routes for an Event Management Software

# Import
from flask import Flask, jsonify, request
from event_info import events_list
from utils import search_event, search_by_venue

app = Flask(__name__)

# Define routes to different API endpoints
@app.route('/')
def home():
    return "Hello this is the homepage"

#Endpoint to list all flights
@app.route('/events')
def events():
    return jsonify(events_list)

# Endpoint to get an event by event ID
@app.route('/events/<int:eventID>')
def get_event_by_ID(eventID):
    event_lookedup = search_event(eventID, events_list)
    return jsonify(event_lookedup)

# Endpoint to search events by venue
@app.route('/events/venuesearch/<path:venuepicked>')
def get_event_by_venue(venuepicked):
    venue_with_spaces = venuepicked.replace('_', ' ')
    venue_lookedup = search_by_venue(venue_with_spaces, events_list)
    return jsonify(venue_lookedup)

# # Endpoint to add a new event
@app.route('/events', methods=['POST'])
def add_event():
    event = request.get_json()
    events_list.append(event)
    return event

if __name__ == '__main__':
    app.run(debug=True)



# Define endpoint to get events with more than 10 seats remaining
@app.route('/events/more_than_10_seats')
def get_events_with_more_than_10_seats():
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor(dictionary=True)

        # SQL query to select events with more than 10 seats remaining
        query = "SELECT * FROM events WHERE remaining_seats > 10"
        cursor.execute(query)

        # Fetch all results
        events = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        db_connection.close()

        # Return JSON response
        return jsonify(events)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)