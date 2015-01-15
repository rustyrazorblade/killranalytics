from flask import Flask

class ExtendedFlask(Flask):
    pass

app = Flask(__name__)


@app.route("/ka/submit", methods=["POST"])
def submit_analytics():
    return "OK"

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
