from webtest import TestApp
from webapp.app import app as flask_app

app = TestApp(flask_app)

def test_whatever():
    response = app.post("/ka/submit", {"name": "jon"})

# def test_slow():
#     import time
#     time.sleep(5)



