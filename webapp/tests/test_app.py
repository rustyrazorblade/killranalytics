from webtest import TestApp
from webapp.app import app as flask_app

app = TestApp(flask_app)

def test_whatever():
    app.post("/ka/submit", {"name": "jon"})
