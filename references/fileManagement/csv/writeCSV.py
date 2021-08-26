# -*- coding: utf-8 -*-
"""
Python Write Txt
omgitskuei
Aug 4th 2021
https://www.kite.com/python/answers/how-to-write-a-csv-file-by-column-in-python
"""
import csv

"""
Write into CSV file in ROWS, and in COLS
"""

headers = ["Country", "Ranking"]
col1 = ["Peru", "Congo", "Belgium", "Thailand"]
col2 = [1, 2, 3, 4]


file = open("testWriteCSV.txt", "w", encoding='UTF8')

writer = csv.writer(file)   # create the csv writer

writer.writerow(headers)

maxWidth = len(col1)
for w in range(maxWidth):   # iterate through integers 0-3
    writer.writerow([col1[w], col2[w]])

# Result: testWriteCSV.TXT
# ----------------------
# "Country", "Ranking"
# Peru,1
# Congo,2
# Belgium,3
# Thailand,4

file.close()


header = ['name', 'area', 'country_code2', 'country_code3']
country1 = ['Afghanistan', 652090, 'AF', 'AFG']
country2 = ['Taiwan', 696969, 'TW', 'TWN']

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(country1)   # Note this adds an empty row at the end
    writer.writerow(country2)   # if newline isn't specified


header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countriesV2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
