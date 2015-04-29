from sys import path
path.append(".")

from cassandra.cqlengine.management import sync_table, create_keyspace

from killranalytics.models import connect_cassandra, PageViews, RealTimeData

connect_cassandra()

ks = 'killranalytics'
create_keyspace(ks, "SimpleStrategy", 1)

sync_table(PageViews)
sync_table(RealTimeData)


print "done"
