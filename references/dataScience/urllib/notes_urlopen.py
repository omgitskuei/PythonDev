# -*- coding: utf-8 -*-
"""
Program name: notes_urlopen
Summary: My notes on urllib.request urlopen, from
'Web Scraping with Python, 2nd Edition, Ryan Mitchell, O'Reilly'
Created on: Fri Dec 24 23:57:00 2021
@author: omgitskuei (Github)
"""


"""
urllib is a standard Python library (meaning you don’t have to install anything extra
to run this example) and contains functions for requesting data across the web, han‐
dling cookies, and even changing metadata such as headers and your user agent
"""
from urllib.request import urlopen

"""This outputs the HTML file page1.html, found in the directory <web root>/pages, 
on the server located at the domain name http://pythonscraping.com Why is it 
important to start thinking of these addresses as “files” rather than “pages”? 
Most modern web pages have many resource files associated with them. These could 
be image files, JavaScript files, CSS files, or any other content that the page 
you are requesting is linked to. When a web browser hits a tag such as <img 
src="cuteKit ten.jpg">, the browser knows that it needs to make another request to 
the server to get the data at the file cuteKitten.jpg in order to fully render the 
page for the user. Of course, your Python script doesn’t have the logic to go back 
and request multiple files (yet); it can only read the single HTML file that 
you’ve directly requested. """
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

html = urlopen('http://google.com/')
print(html.read())
