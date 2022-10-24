from flask import Flask
from flask import make_response
from flask import request

from flask_api.status import HTTP_400_BAD_REQUEST
from flask_api.status import HTTP_200_OK

from utils.date_parser import DateParser

from service.events_service import EventsService


# constants
DAY = "day"
MONTH = "month"
GET = "GET"

# initialize new Flask application
app = Flask(__name__)

@app.route("/events", methods=[GET])
def events():
    # get request body as JSON object
    req = request.json

    # create list of request object attributes
    req_attributes = list(req.keys())
    # if any required attributes are missing send reponse with status 400
    if (not DAY in req_attributes) or (not MONTH in req_attributes):
        return make_response(
            { "Error": "Request object missing 1 or more required attributes" },
            HTTP_400_BAD_REQUEST
        )

    # get events for day and month in request object
    try:
        events = EventsService(DateParser()).get_events(req[DAY], req[MONTH])
    except ValueError:
        return make_response(
            { "Error": "Request object contains 1 or more misconfigured attribute values" },
            HTTP_400_BAD_REQUEST
        )

    return make_response({}, HTTP_200_OK)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
