from cqlengine import Model
from cqlengine.columns import *

class User(Model):
    __table_name__ = 'user'
    user_id = UUID(primary_key=True)
    name = Text()

class Site(Model):
    __table_name__ = 'site'
    site_id = UUID(primary_key=True)
    name = Text()

class Page(Model):
    # url path
    # we want all paths for a given site to be in the same partition
    __table_name__ = 'url'
    site_id = UUID(primary_key=True)
    page_id = Text(primary_key=True)


class RawPageViews(Model):
    # for a given page on a site
    __table_name__ = 'raw_page_views'
    site_id = UUID(primary_key=True, partition_key=True)
    page_id = Text(primary_key=True, partition_key=True)

    # keep the newest stuff first
    view_id = TimeUUID(primary_key=True, clustering_order="DESC")


class HourlyRollupByPage(Model):
    # for a given site & page, what are the stats
    # sparse table - no data, no entry
    # contains 1 hour of data, bucketed into seconds, so up to 3600 records
    __table_name__ = "minute_rollup_by_site"
    site_id = UUID(primary_key=True, partition_key=True)


class HourlyRollupBySite(Model):
    __table_name__ = "minute_rollup_by_site"
    site_id = UUID(primary_key=True, partition_key=True)
    day = Date(primary_key=True, partition_key=True)
    hour = Integer(primary_key=True)



