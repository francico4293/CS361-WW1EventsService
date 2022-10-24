from flask import Flask
from flask import make_response
from flask import request

from flask_api import status

from constants.common_constants import CommonConstants
DAY = CommonConstants.DAY
MONTH = CommonConstants.MONTH


# initialize new Flask application
app = Flask(__name__)

@app.route("/events", methods=["GET"])
def events():
    # get request body as JSON object
    req = request.json

    # create list of request object attributes
    req_attributes = list(req.keys())
    # if any required attributes are missing send reponse with status 400
    if (not DAY in req_attributes) or (not MONTH in req_attributes):
        return make_response(
            { "Error": "Request object missing 1 or more required attributes" },
            status.HTTP_400_BAD_REQUEST
        )

    return "Hello from Flask"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
