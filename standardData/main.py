import numpy as np
import pandas as pd
import csv
import re

PATH_ALO_NHA_DAT = "../crawlData/alonhadat.csv"
PATH_BAT_DONG_SAN_SO = "../crawlData/batdongsanso.csv"
PATH_IBAT_DONG_SAN = "../crawlData/ibatdongsan.csv"
PATH_NHA_DAT_24H= "../crawlData/nhadat24h.csv"

alonhadat = pd.read_csv(PATH_ALO_NHA_DAT, encoding = 'utf-8')
batdongsanso = pd.read_csv(PATH_BAT_DONG_SAN_SO, encoding = 'utf-8')
ibatdongsan = pd.read_csv(PATH_IBAT_DONG_SAN, encoding = 'utf-8')
nhadat24h = pd.read_csv(PATH_NHA_DAT_24H, encoding = 'utf-8')

#loại bỏ trùng lặp
def dropDuplicate(data, subset) :
    return data.drop_duplicates(subset= subset)

alonhadat = dropDuplicate(alonhadat, ['address', 'project', 'type', 'direct', 'price', 'square', 'bedroom', 'floor', 'diningroom', 'kitchen'])
batdongsanso = dropDuplicate(batdongsanso, ['address', 'price', 'district', 'property'])
ibatdongsan = dropDuplicate(ibatdongsan, ['address', 'type', 'direct', 'price', 'length', 'width', 'area', 'bedroom', 'floor', 'world_highway'])
nhadat24h = dropDuplicate(nhadat24h, ['address', 'type', 'direct', 'price', 'ground_area', 'usable_area', 'kitchen', 'livingroom', 'name_project', 'specific_address'])

class Standard:
    def __init__(self, data):
        self.data = data

    # tách trường address thành các trường ward, province, street, district
    def sliceAddress(self, fieldAddress):
        lsStreet = []
        lsWard = []
        lsDistrict = []
        lsProvince = []

        for item in self.data[fieldAddress]:
            street = self.sliceStringByString(item, "Đường") or self.sliceStringByString(item, "Phố")
            lsStreet.append(street)

            idxStartProvince = item.rfind(',') + 1
            province =item[idxStartProvince:]
            lsProvince.append(province)

            ward = self.sliceStringByString(item, "Phường") or self.sliceStringByString(item, "Xã")
            lsWard.append(ward)

            district = self.sliceStringByString(item, "Quận") or self.sliceStringByString(item, "Huyện")
            lsDistrict.append(district)

        self.data["ward"] = lsWard
        self.data["district"] = lsDistrict
        self.data["province"] = lsProvince
        self.data["street"] = lsStreet
        self.data = self.data.drop(columns=[fieldAddress])

    # tách string bằng string
    def sliceStringByString(self, s, sub):
        startIndex = s.find(sub)
        if startIndex != -1:
            startIndex = startIndex + len(sub)
            endIndex = s[startIndex:].find(',')
            if endIndex != -1:
                return s[startIndex:][:endIndex]
            else:
                return s[startIndex:]
        return None

    #chuyển tiếng việt có dấu thành tiếng việt k dấu
    # def noAccent(self, fields):
    #     for field in fields:
    #         ls = []
    #         for item in self.data[field]:
    #             item = no_accent_vietnamese(item)
    #             ls.append(item)
    #         self.data[field] = ls

    #bỏ đơn vị đo lường : m
    def removeUnitMeasure(self, fields):
        for field in fields:
            ls = []
            for item in self.data[field]:
                item = re.findall(r"(?:\d*\.\d+|\d+)", item)
                if len(item):
                    item = item[0]
                else:
                    item = None
                ls.append(item)
            self.data[field] = ls

    # Chuẩn hóa đơn vị cho price theo đồng
    def standardPrice(self, fieldPrice, fieldSquare):
        ls = []
        for price, square in zip(self.data[fieldPrice], self.data[fieldSquare]):
            price = re.sub(",",".",price)
            valPrice = re.findall(r"(?:\d*\.\d+|\d+)", price)
            if(valPrice):
                valPrice = float(valPrice[0])
                if "/m" in price:
                     valPrice = valPrice * float(square)
                if "/tháng" in price:
                    valPrice = None
                else:
                    if "tỷ" in price:
                        valPrice = valPrice * 1000000000

                    if "triệu" in price:
                        valPrice = valPrice * 1000000
            else: valPrice = None
            ls.append(str(valPrice))
        self.data[fieldPrice] = ls

    # Chuẩn hóa date về dạng dd/mm/yyyy
    def standardDate(self, fieldDate):
        ls = []
        for item in self.data[fieldDate]:
            date = re.sub('-','/',item)
            date = re.search(r'\d{2}/\d{2}/\d{4}', date)
            if (date):
                date = date.group(0)
            else:
                if "Hôm nay" in item:
                    date = "26/05/2022"
                if "Hôm qua" in item:
                    date = "25/05/2022"
            ls.append(date)
        self.data[fieldDate] = ls

    #Chuẩn hóa giá tị None, field nào toàn None thì sẽ bị loại bỏ
    def standardNone(self, fields):
        for field in fields:
            ls = []
            for item in self.data[field]:
                if item =="_" or item == "---":
                    item = None
                ls.append(item)
            if len(ls):
                self.data[field] = ls
            else :
                self.data = self.data.drop(columns=field)

alo = Standard(alonhadat)
alo.sliceAddress("address")
alo.standardDate("date")
# alo.noAccent(["description", "juridical", "name_contact", "title", "type", "project"])
alo.removeUnitMeasure(["square", "length", "width", "road_width"])
alo.standardPrice("price", "square")
alo.standardNone(["direct", "floor", "juridical", "length", "road_width"])
alo.data.to_csv("alonhadat.csv")


ibds = Standard(ibatdongsan)
ibds.sliceAddress("address")
ibds.standardDate("date")
ibds.removeUnitMeasure(["area", "length", "width", "world_highway"])
ibds.standardPrice("price", "area")
ibds.standardNone(["diningroom", "direct", "floor", "kitchen", "parking", "terrace", "width", "juridical", "length", "world_highway"])
ibds.data.to_csv("ibatdongsan.csv")

nd24h = Standard(nhadat24h)
nd24h.sliceAddress("address")
nd24h.standardDate("date")
nd24h.removeUnitMeasure(["ground_area", "length", "width", "road_width", "usable_area"])
nd24h.standardPrice("price", "ground_area")
nd24h.standardNone(["road_width","juridical"])
nd24h.data.to_csv("nhadat24h.csv")

