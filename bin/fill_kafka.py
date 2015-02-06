from sys import path, argv
path.append("")

import time
import json
from uuid import uuid4
import random


from webapp.models import PageViews

# collect metrics for 10 sites
sites = [str(uuid4()) for x in range(10)]
pages = ["/index.html", "/archive.php", "/whatever.js", "/something.css"]

try:
    per_second = float(argv[1])
except:
    print "Using default of 5 / sec"
    per_second = 5.0

rate = 1 / per_second

print rate

for x in range(1000):
    print PageViews.create(random.choice(sites),
                           random.choice(pages),
                           None)
    time.sleep(rate)
