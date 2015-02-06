from sys import path
path.append("")

import time
import json
from uuid import uuid4
import random


from webapp.models import PageViews

# collect metrics for 10 sites
sites = [str(uuid4()) for x in range(10)]
pages = ["/index.html", "/archive.php", "/whatever.js", "/something.css"]

for x in range(100):
    print PageViews.create(random.choice(sites),
                           random.choice(pages),
                           None)
    time.sleep(.2)
