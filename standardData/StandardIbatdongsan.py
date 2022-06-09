from standardData.StandardCommon import StandardCommon
import pandas as pd

class StandardIbatdongsan(StandardCommon):
    def __init__(self, data):
        self.data = data

PATH_IBAT_DONG_SAN = "../crawlData/ibatdongsan.csv"
ibatdongsan = pd.read_csv(PATH_IBAT_DONG_SAN, encoding = 'utf-8')

ibds = StandardIbatdongsan(ibatdongsan)
ibds.dropDuplicate(['address', 'type', 'direct', 'price', 'length', 'width', 'area', 'bedroom', 'floor', 'world_highway'])
ibds.sliceAddress("address")
ibds.standardDate("date")
ibds.removeUnitMeasure(["area", "length", "width", "world_highway"])
ibds.standardPrice("price", "area")
ibds.standardNone(["diningroom", "direct", "floor", "kitchen", "parking", "terrace", "width", "juridical", "length", "world_highway"])
ibds.data.to_csv("ibatdongsan.csv")
