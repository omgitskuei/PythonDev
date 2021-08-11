"""
Python Write Txt
omgitskuei
Aug 11th 2021
https://www.kite.com/python/answers/how-to-write-a-csv-file-by-column-in-python
"""

import csv

with open('countriesV2.csv', newline='') as csvFile:
    print(type(csvFile))
    # <class '_io.TextIOWrapper'>

    readerObj = csv.reader(csvFile, delimiter=',')

    print(type(readerObj))
    # <class '_csv.reader'>

    for line in readerObj:
        print(line)
    # ['name', 'area', 'country_code2', 'country_code3']
    # ['Albania', '28748', 'AL', 'ALB']
    # ['Algeria', '2381741', 'DZ', 'DZA']
    # ['American Samoa', '199', 'AS', 'ASM']
    # ['Andorra', '468', 'AD', 'AND']
    # ['Angola', '1246700', 'AO', 'AGO']

    # Convert type from csv.reader to list/tuple for more functionality
    print('Convert type from csv.reader to list')
    aList = list(readerObj)
    print(aList)
    # []
    # NOTE: aList is empty because _io.TextIOWrapper needs to
    # reset to start of file after iteration

    # Resets the file
    csvFile.seek(0)
    print('Convert type from csv.reader to tuple')
    aTuple = tuple(readerObj)
    print(aTuple)
    # (
    # ['name', 'area', 'country_code2', 'country_code3'],
    # ['Albania', '28748', 'AL', 'ALB'],
    # ['Algeria', '2381741', 'DZ', 'DZA'],
    # ['American Samoa', '199', 'AS', 'ASM'],
    # ['Andorra', '468', 'AD', 'AND'],
    # ['Angola', '1246700', 'AO', 'AGO']
    # )
    print(aTuple[1][0])
    # Albania

    csvFile.close()
