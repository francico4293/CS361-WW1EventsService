from flask import Flask
from flask import make_response
from flask import request


# initialize new Flask application
app = Flask(__name__)

@app.route("/events", methods=["GET"])
def events():
    req = request.json

    req_attributes = list(req.keys())
    if (not "day" in req_attributes) or (not "month" in req_attributes):
        return make_response(
            { "Error": "Request object missing 1 or more required attributes" },
            400
        )

    return "Hello from Flask"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
