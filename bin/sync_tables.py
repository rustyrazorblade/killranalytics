from sys import path
path.append(".")

from cqlengine.management import sync_table, create_keyspace

from webapp.models import connect_cassandra, PageViews, RealTimeData

connect_cassandra()

create_keyspace(ks, "SimpleStrategy", 1)

sync_table(PageViews)
sync_table(RealTimeData)


print "done"
