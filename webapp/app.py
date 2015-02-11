from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template
from models import PageViews, connect_cassandra, connect_kafka

from kafka import SimpleConsumer

# we're pushing everything into a topic called raw
from flask.ext.uuid import FlaskUUID

class ExtendedFlask(Flask):
    pass

app = ExtendedFlask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")
FlaskUUID(app)

from flask.ext.uwsgi_websocket import GeventWebSocket
ws = GeventWebSocket(app)


##### ROUTES BELOW HERE ########

kafka = None

@app.before_first_request
def connect_to_db():
    global kafka
    print "Connecting to cassandra"
    try:
        connect_cassandra()
    except Exception as e:
        print e

    print "Connecting to kafka"
    kafka = connect_kafka()
    print "done with connecting"



@app.route("/ka/submit", methods=["POST"])
def submit_analytics():
    # should put a message into kafka and return asap
    PageViews.create()
    return "OK"

@app.route("/")
def index():
    # shows the dashboard
    # if the user is not logged in, kick them to the login page
    return render_template("index.tpl")



@app.route("/stream/<uuid:stream_id>")
def stream(stream_id):
    return render_template("stream.tpl")

#
# @app.route("/login")
# def login():
#     return render_template("login.tpl")


@ws.route("/stream_ws")
def stream_ws(ws):
    global kafka
    # get the stream_id we're going to follow
    msg = ws.receive()
    topic = "live_updates.{}".format(msg)

    from uuid import uuid4

    kafka = connect_kafka()
    consumer = SimpleConsumer(kafka, None, topic, auto_commit=False)

    while True:
        print "Fetching"
        try:
            msg = consumer.get_messages()[0].message.value
            ws.send(msg)
            print "sent"
        except Exception as e:
            print e
            print "nothing waiting"


# if __name__ == "__main__":
#     app.run(host='localhost', port=8080, debug=True)
