from flask import Flask, render_template

class ExtendedFlask(Flask):
    pass

app = ExtendedFlask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")


@app.route("/ka/submit", methods=["POST"])
def submit_analytics():
    return "OK"

@app.route("/")
def index():
    # shows the dashboard
    return render_template("index.tpl")

@app.route("/login")
def login():
    return render_template("login.tpl")

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
