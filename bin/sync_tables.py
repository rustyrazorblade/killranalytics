from sys import path
path.append(".")

from cqlengine.management import sync_table

from webapp.models import connect, PageViews

connect()
sync_table(PageViews)


print "done"
