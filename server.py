from flask import Flask


# initialize new Flask application
app = Flask(__name__)

@app.route("/events", methods=["GET"])
def events():
    return "Hello from Flask"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
