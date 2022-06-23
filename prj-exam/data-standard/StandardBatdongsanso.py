from .StandardCommon import StandardCommon
import pandas as pd
import re

class StandardBatdongsanso(StandardCommon):
    def __init__(self, data):
        self.data = data

    def standardPhoneContact(self, field):
        ls = []
        for item in self.data[field]:
            item = re.sub("\*", "X", item)
            ls.append(item)
        self.data[field] = ls

    def standardAddress(self, field):
        ls = []
        for item in self.data[field]:
            item = item.strip()
            item = item[1:]
            item = re.sub("\n", "", item)
            ls.append(item)
        self.data[field] = ls

    def sliceProperty(self, fieldProperty, fieldSquare, fieldDirect, fieldBedroom, fieldToilet, fieldFacade, fieldFloor):
        lsSquare = []
        lsDirect= []
        lsBedroom = []
        lsToilet = []
        lsFacade = []
        lsFloor = []

        for item in self.data[fieldProperty]:
            item = re.sub(":", "", item)
            square = self.sliceStringByString(item, "Diện tích")
            direct = self.sliceStringByString(item, "Hướng")
            bedroom = self.sliceStringByString(item, "Số phòng ngủ")
            toilet = self.sliceStringByString(item, "Số toilet")
            facade = self.sliceStringByString(item, "Mặt tiền")
            floor = self.sliceStringByString(item, "Số tầng")

            lsSquare.append(square)
            lsDirect.append(direct)
            lsBedroom.append(bedroom)
            lsToilet.append(toilet)
            lsFacade.append(facade)
            lsFloor.append(floor)

        self.data[fieldSquare] = lsSquare
        self.data[fieldDirect] = lsDirect
        self.data[fieldBedroom] = lsBedroom
        self.data[fieldToilet] = lsToilet
        self.data[fieldFacade] = lsFacade
        self.data[fieldFloor] = lsFloor
        self.data = self.data.drop(columns=fieldProperty)


PATH_BAT_DONG_SAN_SO = "../data-raw/batdongsanso.csv"
batdongsanso = pd.read_csv(PATH_BAT_DONG_SAN_SO, encoding = 'utf-8')

bdss = StandardBatdongsanso(batdongsanso)

bdss.sliceProperty("property", "square", "direct", "bedroom", "toilet", "facade", "floor")
bdss.standardDate("date")
bdss.removeUnitMeasure(["square"])
bdss.standardPrice("price", "square")
bdss.standardType("type")
bdss.standardPhoneContact("phone_contact")
bdss.standardAddress("address")
bdss.strip(["name_contact", "direct"])
bdss.dropDuplicate(['address', 'price', 'bedroom', 'floor', "facade", "toilet", "direct", "square"])

bdss.data.to_csv("batdongsanso.csv")