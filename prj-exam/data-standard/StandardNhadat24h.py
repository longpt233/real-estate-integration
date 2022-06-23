from .StandardCommon import StandardCommon
import pandas as pd
import numpy as np
import re

class StandardNhadat24h(StandardCommon):
    def __init__(self, data):
        self.data = data

    def standardDirect(self, field):
        ls = []
        for item in self.data[field]:
            item = item.strip()
            if item == "Không xác định":
                item = None
            ls.append(item)
        self.data[field] = ls

    def standardAddress(self, field):
        ls = []
        for item in self.data[field]:
            item = str(item)
            item = item.strip()
            item = re.sub("\n+", "", item)
            item = re.sub(' +', " ", item)
            ls.append(item)
        self.data[field] = ls

PATH_NHA_DAT_24H= "../data-raw/nhadat24h.csv"
nhadat24h = pd.read_csv(PATH_NHA_DAT_24H, encoding = 'utf-8')

nd24h = StandardNhadat24h(nhadat24h)

# nd24h.sliceAddress("address")
nd24h.standardDate("date")
nd24h.removeUnitMeasure(["ground_area", "length", "width", "road_width", "usable_area"])
nd24h.standardPrice("price", "ground_area")
nd24h.standardNone(["juridical"])
nd24h.standardDirect("direct")
nd24h.standardType("type")
nd24h.standardAddress("address")
nd24h.standardAddress("specific_address")
nd24h.dropDuplicate(['address', 'type', 'direct', 'price', 'ground_area', 'usable_area', 'kitchen', 'livingroom', 'name_project', 'specific_address'])

nd24h.data.to_csv("nhadat24h.csv")
