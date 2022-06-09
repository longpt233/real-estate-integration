from standardData.StandardCommon import StandardCommon
import pandas as pd
import numpy as np

class StandardNhadat24h(StandardCommon):
    def __init__(self, data):
        self.data = data



PATH_NHA_DAT_24H= "../crawlData/nhadat24h.csv"
nhadat24h = pd.read_csv(PATH_NHA_DAT_24H, encoding = 'utf-8')

nd24h = StandardNhadat24h(nhadat24h)
nd24h.dropDuplicate(['address', 'type', 'direct', 'price', 'ground_area', 'usable_area', 'kitchen', 'livingroom', 'name_project', 'specific_address'])
nd24h.sliceAddress("specific_address")
nd24h.standardDate("date")
nd24h.removeUnitMeasure(["ground_area", "length", "width", "road_width", "usable_area"])
nd24h.standardPrice("price", "ground_area")
nd24h.standardNone(["road_width","juridical"])
nd24h.data.to_csv("nhadat24h.csv")