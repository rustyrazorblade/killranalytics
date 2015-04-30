#!/usr/bin/env python

from blessings import Terminal
import collections
from kafka import KafkaConsumer

site = "02559c4f-ec20-4579-b2ca-72922a90d0df"

class DrawState(object):
    term = None
    latest_samples = None
    consumer = None

    def __init__(self, term):
        self.term = term
        self.latest_samples = collections.deque(maxlen=20)
        self.consumer = KafkaConsumer("")

    def draw(self):
        # read in any state from kafka
        self.draw_hits_graph()

    def draw_hits_graph(self):
        pass



def main():
    term = Terminal()
    ds = DrawState(term)
    while True:
        ds.draw()
