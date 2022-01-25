# -*- coding: utf-8 -*-
"""
Program name: notes_bs
Summary: My notes on BeautifulSoup, from
'Web Scraping with Python, 2nd Edition, Ryan Mitchell, O'Reilly'
Created on: Fri Dec 25 12:57:00 2021
@author: omgitskuei (Github)
"""

# beautiful_soup isn't a default Python library, needs to be installed with
# pip install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup

# get HTML file via urllib
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
print(html)
# <http.client.HTTPResponse object at 0x03D677F0>
print(type(html))
# <class 'http.client.HTTPResponse'>

htmlRead = html.read()
print(htmlRead)\
# b'<html>\n
#     <head>\n
#         <title>A Useful Page</title>\n
#     </head>\n
#     <body>\n
#         <h1>An Interesting Title</h1>\n
#         <div>\nLorem ipsum dolor sit amet, consectetur adipisici ...\n</div>\n
#     </body>\n
# </html>\n'
print(type(htmlRead))
# <class 'bytes'>

'''
BeautifulSoup object takes two arguments;
1)    html file, or html text
2)    a name of the parser* used

*For most cases, which parser doesn't make a huge difference:
1)    'html.parser'
1a)   comes included with Python 3, no installations needed.

2)    'lxml'
2a)   generally better at parsing malformed HTML (unclosed/improperly nested tags)
2b)   marginally faster than html.parser
2c)   must be installed separately
        $ pip3 install lxml
        bs = BeautifulSoup(html, ‘lxml’)
2d)   depends on 3rd party C libraries, portability problems

3)    'html5lib'
3a)   like lxml, but goes further to correct broken HTML
3b)   slower than both html.parser & lxml
3c)   must be installed separately
3d)   may be an option parsing handwritten HTML sites
        bs = BeautifulSoup(html.read(), ‘html5lib’);
'''

# In[1] - Read HTML file then scrap
bs = BeautifulSoup(htmlRead, 'html.parser')

print("BeautifulSoup(html.read(), 'html.parser')")
print(bs)
# <html>
# <head>
# <title>A Useful Page</title>
# </head>
# <body>
# <h1>An Interesting Title</h1>
# <div>
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiu...
# </div>
# </body>
# </html>

print(type(bs))
# <class 'bs4.BeautifulSoup'>

# retrieve elements from HTML
print(bs.h1)            # Note: returns the FIRST instance, not all <h1></h1>s
# <h1>An Interesting Title</h1>

print(type(bs.h1))
# <class 'bs4.element.Tag'>

# Note: h1 returned is 2 layers deep (html -> body -> h1), but we can fetch it by
# calling the h1 tag directly
print(bs.html.body.h1)  # full path
print(bs.body.h1)
print(bs.html.h1)
print(bs.h1)
# Note: all of these fetch the same h1 tag




# In[2] - scrap from html file without calling .read()
html2 = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs2 = BeautifulSoup(html, 'html.parser')

print("BeautifulSoup(html, 'html.parser')")
print(bs2)
# <html>
# <head>
# <title>A Useful Page</title>
# </head>
# <body>
# <h1>An Interesting Title</h1>
# <div>
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tem...
# </div>
# </body>
# </html>
print(type(bs2))
# <class 'bs4.BeautifulSoup'>

print(id(bs))
print(id(bs2))
# the two objects have different IDs

print(bs == bs2)
# false
