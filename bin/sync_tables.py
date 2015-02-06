from sys import path
path.append(".")

from cqlengine.management import sync_table

from webapp.models import connect_cassandra, connect_kafka, PageViews

connect_cassandra()

sync_table(PageViews)


print "done"
