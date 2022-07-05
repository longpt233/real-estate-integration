import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import numpy as np
import re

data = pd.read_csv("final_data_full_feature.csv", index_col=False, delimiter = ',')
ls = []
for item in data["square"]:
    item = re.findall(r"(?:\d*\.\d+|\d+)", item)
    if len(item):
        item = float(item[0])
        ls.append(item)
    else:
        item = float(0)
        ls.append(item);
data = data.replace(np.nan,"")

data["square"] = ls
try:
    conn = mysql.connect(host='localhost', database='intergration', user='root', password='')

    if conn.is_connected():
        cursor = conn.cursor()

        #loop through the data frame
        for i,row in data.iterrows():
            sql = "INSERT INTO house (title, description, price, square, name_contact, phone_contact, date" \
                  ", direct, street, floor, juridical, bedroom, length, width, link_image, url_page, kitchen, parking,terrace," \
                  " type, district, province, ward ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()

except Error as e:
            print("Error while connecting to MySQL", e)