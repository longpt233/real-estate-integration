from standardData.StandardCommon import StandardCommon
import pandas as pd
import numpy as np

class StandardAlonhadat(StandardCommon):
    def __init__(self, data):
        self.data = data

    def standardIcon(self, fields):
        for field in fields:
            ls = []
            for item in self.data[field]:
                if item == "/publish/img/check.gif":
                    ls.append("Có")
                else:
                    ls.append(None)
            self.data[field] = ls


PATH_ALO_NHA_DAT = "../crawlData/alonhadat.csv"
alonhadat = pd.read_csv(PATH_ALO_NHA_DAT, encoding = 'utf-8')

alonhadat = StandardAlonhadat(alonhadat)
alonhadat.dropDuplicate(['address', 'project', 'type', 'direct', 'price', 'square', 'bedroom', 'floor', 'diningroom', 'kitchen'])
alonhadat.sliceAddress("address")
alonhadat.standardDate("date")
alonhadat.removeUnitMeasure(["square", "length", "width", "road_width"])
alonhadat.standardPrice("price", "square")
alonhadat.standardType("type")
alonhadat.standardNone(["direct", "floor", "juridical", "length", "road_width"])
alonhadat.standardIcon(["kitchen", "diningroom", "parking", "terrace"])
alonhadat.data.to_csv("alonhadat.csv")