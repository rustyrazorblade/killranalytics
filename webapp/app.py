from flask import Flask, render_template

class ExtendedFlask(Flask):
    pass

app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")


@app.route("/ka/submit", methods=["POST"])
def submit_analytics():
    return "OK"

@app.route("/")
def index():
    return render_template("base.tpl")

@app.route("/login")
    return render_template("login.tpl")

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
