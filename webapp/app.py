from flask import Flask, render_template
from models import RawPageViews

from kafka import KafkaClient, SimpleProducer, SimpleConsumer

# To send messages synchronously
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

# we're pushing everything into a topic called raw
from flask.ext.uuid import FlaskUUID

class ExtendedFlask(Flask):
    pass

app = ExtendedFlask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")
FlaskUUID(app)


@app.route("/ka/submit", methods=["POST"])
def submit_analytics():
    # should put a message into kafka and return asap
    return "OK"


@app.route("/")
def index():
    # shows the dashboard
    # if the user is not logged in, kick them to the login page
    return render_template("index.tpl")


@app.route("/stream")
@app.route("/stream/<uuid:stream_id>")
def stream():
    return render_template("stream.tpl")


@app.route("/login")
def login():
    return render_template("login.tpl")


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
