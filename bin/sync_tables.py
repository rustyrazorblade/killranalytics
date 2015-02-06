from sys import path
path.append(".")

from cqlengine.management import sync_table

from webapp.models import connect_cassandra, PageViews, RealTimeData

connect_cassandra()

sync_table(PageViews)
sync_table(RealTimeData)


print "done"
