from .StandardCommon import StandardCommon
import pandas as pd

class StandardIbatdongsan(StandardCommon):
    def __init__(self, data):
        self.data = data
        self.baseURL = "http://i-batdongsan.com"

    def standardLinkImage(self, field):
        ls = []
        for item in self.data[field]:
            item = self.baseURL + str(item)
            ls.append(item)
        self.data[field] = ls

PATH_IBAT_DONG_SAN = "../data-raw/ibatdongsan.csv"
ibatdongsan = pd.read_csv(PATH_IBAT_DONG_SAN, encoding = 'utf-8')

ibds = StandardIbatdongsan(ibatdongsan)
# ibds.sliceAddress("address")
ibds.standardDate("date")
ibds.removeUnitMeasure(["area", "length", "width", "world_highway"])
ibds.standardPrice("price", "area")
ibds.standardNone(["diningroom", "direct", "floor", "kitchen", "parking", "terrace", "width", "juridical", "length", "world_highway", "bedroom"])
ibds.standardType("type")
ibds.standardIcon(["diningroom", "kitchen", "parking", "terrace"])
ibds.standardLinkImage("link_image")
ibds.dropDuplicate(['address', 'type', 'direct', 'price', 'length', 'width', 'area', 'bedroom', 'floor', 'world_highway'])

ibds.data.to_csv("ibatdongsan.csv")
