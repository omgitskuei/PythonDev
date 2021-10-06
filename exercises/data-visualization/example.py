# -*- coding: utf-8 -*-
"""
Program name: visualizeExample
Summary: Using numpy, panda, and matplotlib to visualize/graph data
Created on: Wed Oct  6 19:05:47 2021
@author: omgitskuei (Github)
"""

# matplotlib for visualization, numpy and pandas for modeling data
# these accronyms are industry standards; np, pd, plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# In[1]
"""
matplotlib.pyplot
"""
# example data used
arr1 = [105, 118, 120, 130, 140]
arr2 = [55, 68, 70, 80, 30]
years = [2017, 2018, 2019, 2020, 2021]

# using pyplot to graph the data into a line graph
# line graph; plot([data for x axis], [data for y axis])
plt.plot(years, arr1, color="#ff0000")
plt.plot(years, arr2)
plt.show

# In[2]
"""
numpy
"""
# transform array into dataframe with pd
# example data used
arr3 = np.array(
    [
        (2, 4, 6, 8),
        (30, 40, 50, 60)
    ]
)

df = pd.DataFrame(arr3)
print(df)
"""
returns;
0   1   2   3
0   2   4   6   8
1  30  40  50  60
"""

df = pd.DataFrame(
    arr3,
    index=["A", "B"],
    columns=["col1", "col2", "col3", "col4"])
print(df)
"""
col1  col2  col3  col4
A     2     4     6     8
B    30    40    50    60
"""

# graph df as line graph
df.plot()


# customizing color of bars in a bar graph
df.plot.bar(
    color=(
        "#ff0000",     # red color specified for column 1
        "#00ff00",     # green color specified for column 1
        "#0000ff",     # blue color specified for column 1
        "#ff00ff")     # magenta color specified for column 1
)

plt.savefig("chart_01.png", dpi=300, format="png")
plt.close()


# In[3]

# example data
arrIncome = np.array([
    # 收入, 支出
    (50000, 20000),
    (60000, 90000)
])
arrRows = ['John', 'Ben']
arrCols = ['收入', '支出']

# note this and ...
df = pd.DataFrame(arrIncome,
                  arrRows,
                  arrCols
                  )

# ... this, is the same
df = pd.DataFrame(arrIncome,
                  ['John', 'Ben'],
                  ['收入', '支出']
                  )

# graph as line graph, note this may cause errors since pd can't write chinese
# without config
df.plot()

# one possible chinese font for WINDOWS
plt.rcParams['font.family'] = "Microsoft JhengHei"
df.plot()

# one possible chinese font for APPLE
# plt.rcParams['font.family'] = "AppleGothic"
# plt.rcParams['font.family'] = "Noto Sans TC Light"

# In[4]
import matplotlib.font_manager

listOfAllFonts = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
# print(type(listOfAllFonts)) # list

for i in listOfAllFonts:
    print(i)

# In[5]
import matplotlib
# prints where matplotlib is installed
print(matplotlib.__file__)     # D:\Coding\Spyder\pkgs\matplotlib\__init__.py

# D:\Coding\Spyder\pkgs\matplotlib\mpl-data\fonts\ttf
# is the folder where all usable fonts are located
# useful for adding fonts you want to use that aren't already there.


# In[6]

# randint(min, max, structure(eg. 5 rows, 2 cols))
arr = np.random.randint(10000, 50000, size=(5,2))
print(arr)
# eg;
# [[49787 49976]
# [19823 27159]
# [31069 14040]
# [25769 44175]
# [26544 45161]]

# note; the min, max are inclusive
arr = np.random.randint(1, 6, size=(10, 6))
print(arr)
# eg;
# [[1 1 2 5 3 4]
# [4 2 4 2 2 4]
# [4 4 5 1 2 2]
# [4 4 3 2 4 3]
# [1 3 2 5 1 2]
# [2 1 3 2 5 2]
# [4 1 2 5 2 1]
# [2 5 4 4 2 3]
# [2 5 5 1 1 4]
# [3 4 4 4 2 5]]

df = pd.DataFrame(
    np.random.randint(10000, 50000, size=(5,2)),
    ["A", "B", "C", "D", "E"],
    ["收入", "支出"]
)
print(df)

# In[7]
a = pd.date_range('01/01/2021', periods=5)
print(type(a))    # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
print(a)

a = pd.date_range('01/01/2021', periods=30)
print(a)

a = pd.date_range('01/01/2021', periods=32)
print(a)


b = pd.date_range('01/01/2021', periods=5, freq="M")
print(b)

# freq value defaults to "D" calendar day frequency, other freq values here;
# https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases


# In[8]
# example data
ser_1 = pd.Series(
  [1,2,3,4],
  ['a', 'b', 'c', 'd'],
  name='Chart'
)
# plot pie graph
ser_1.plot.pie()
