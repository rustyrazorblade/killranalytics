from sys import path, argv
path.append("")

import time
import json
from uuid import uuid4
import random


from killranalytics.models import PageViews

# collect metrics for 10 sites
sites = ["02559c4f-ec20-4579-b2ca-72922a90d0df"] # + [str(uuid4()) for x in range(100)]
pages = ["/index.html", "/archive.php", "/whatever.js", "/something.css"]

try:
    per_second = float(argv[1])
except:
    print "Using default of 5 / sec"
    per_second = 5.0

rate = 1 / per_second

print rate

fp = open("kafka.txt", 'w')
for x in range(10000):

    site_id = random.choice(sites)
    page = random.choice(pages)
    print PageViews.create(site_id, page, None)
    fp.write(json.dumps({"site_id":site_id, "page":page}) + "\n")
    time.sleep(rate)
