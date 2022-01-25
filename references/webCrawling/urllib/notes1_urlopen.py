# -*- coding: utf-8 -*-
"""
Program name: notes_urlopen
Summary: My notes on urllib.request urlopen, from
'Web Scraping with Python, 2nd Edition, Ryan Mitchell, O'Reilly'
Created on: Fri Dec 24 23:57:00 2021
@author: omgitskuei (Github)
"""

from urllib.request import urlopen

'''
urllib is a standard Python library (meaning you don’t have to install anything extra
to run this example) and contains functions for requesting data across the web, han‐
dling cookies, and even changing metadata such as headers and your user agent

The urllib.request module defines functions and classes which help in opening URLs 
(mostly HTTP) in a complex world — basic and digest authentication, redirections, 
cookies and more.
See also The Requests package is recommended for a higher-level HTTP client 
interface.
- https://docs.python.org/3/library/urllib.request.html, 2021-12-25
"""


"""This outputs the HTML file page1.html, found in the directory <web root>/pages, 
on the server located at the domain name http://pythonscraping.com 

It is important to think of URL addresses as “files”. 
Most modern web pages have many resource files (img, js, css, etc) 
associated with them. When a web browser hits a tag such as 
<img src="cuteKit ten.jpg">, the browser needs to make another request to 
the server to get the cuteKitten.jpg to fully render the page. 

Of course, your Python script doesn’t have the logic to go back 
and request multiple files (yet); it can only read the single HTML file that 
you’ve directly requested. 
'''

html = urlopen('http://pythonscraping.com/pages/page1.html')

print("html")
print(html)
# <http.client.HTTPResponse object at 0x03901A78>
print("type(html)")
print(type(html))
# <class 'http.client.HTTPResponse'>

print("html.read()")
print(html.read())
# b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An
# Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, consectetur
# adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
# aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
# ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
# voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
# occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
# id est laborum.\n</div>\n</body>\n</html>\n'
print("type(html.read())")
print(type(html.read()))
# <class 'bytes'>

print(id(html.read()))
print(id(html.read()))
# same IDs
