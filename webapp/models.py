from cqlengine import Model
from cqlengine.columns import *
from cqlengine.connection import setup
from cqlengine.management import create_keyspace

from kafka import KafkaClient, SimpleProducer, SimpleConsumer

# To send messages synchronously
kafka = KafkaClient("localhost:9092")
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
    pageview_id = TimeUUID(primary_key=True, clustering_order="DESC")
    page = Text()
    os = Text()
    browser = Text()
    referral = Text()

    # keep the newest stuff first

    @classmethod
    def push(cls, site_id, data):
        """
        we're going to delay our validation of site_id until we pull the data in
        there's no real point in doing it now, and it means we have to talk to the db
        we're going to insert & roll these up in spark

        :param site_id:
        :param data:
        :return:
        """
        pass


class DailyRollupBySite(Model):
    # for a given site & page, what are the stats
    # sparse table - no data, no entry
    # contains 1 hour of data, bucketed into seconds, so up to 3600 records
    __table_name__ = "minute_rollup_by_site"
    site_id = UUID(primary_key=True, partition_key=True)
    day = Date(primary_key=True)

    pageview_id = TimeUUID(primary_key=True, clustering_order="DESC")
    page = Text()
    os = Text()
    browser = Text()
    referral = Text()



def connect():
    # yay for hard coded....
    ks = "killranalytics"
    setup(["localhost"], ks)
    create_keyspace(ks, "SimpleStrategy", 1)
