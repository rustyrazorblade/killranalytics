# built ins
from uuid import uuid1
import json

# cqlengine
from cqlengine import Model
from cqlengine.columns import *

from db import connect_cassandra, connect_kafka
# To send messages synchronously

from kafka import SimpleProducer

connect_cassandra()
kafka = connect_kafka()
producer = SimpleProducer(kafka)


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


class PageViews(Model):
    # for a given page on a site
    __table_name__ = 'pageviews'
    __default_time_to_live__ = 3600 * 24 # just a day?
    __compaction__ = "DateTieredCompactionStrategy"

    site_id = UUID(primary_key=True, partition_key=True)
    pageview_id = TimeUUID(primary_key=True, clustering_order="DESC", default=uuid1)
    page = Text()
    os = Text()
    browser = Text()
    referral = Text()

    # keep the newest stuff first

    @classmethod
    def create(cls, site_id, page, payload):
        """
        we're going to delay our validation of site_id until we pull the data in
        there's no real point in doing it now, and it means we have to talk to the db
        we're going to insert & roll these up in spark

        :param site_id:
        :param payload:
        :return:
        """
        result = super(PageViews, cls).create(site_id=site_id, page=page)

        message = {"site_id": site_id,
                   "page": page }

        producer.send_messages("pageviews", json.dumps(message))

        return result


class DailyRollupBySite(Model):
    # for a given site & page, what are the stats
    # sparse table - no data, no entry
    # contains 1 day of data, bucketed into seconds, so up to 3600 records

    __table_name__ = "daily_rollup_by_site"
    site_id = UUID(primary_key=True, partition_key=True)
    day = Date(primary_key=True, partition_key=True)
    minute = Integer(primary_key=True)

    pageviews = Integer()

    # os = Text()
    # browser = Text()
    # referral = Text()




