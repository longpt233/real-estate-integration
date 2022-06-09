from standardData.StandardCommon import StandardCommon
import pandas as pd
import numpy as np

class StandardBatdongsanso(StandardCommon):
    def __init__(self, data):
        self.data = data

PATH_BAT_DONG_SAN_SO = "../crawlData/batdongsanso.csv"
batdongsanso = pd.read_csv(PATH_BAT_DONG_SAN_SO, encoding = 'utf-8')

bdss = StandardBatdongsanso(batdongsanso)
bdss.dropDuplicate([['address', 'price', 'district', 'property']])