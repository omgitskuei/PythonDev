
'''
Scrapping the web can throw errors;
1) HTTP errors (HTTPError) - page not found on the server
2) server not found (URLError)
3) AttributeError - cannot get data from None existent tag
'''
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http :/ /www.pythonscraping.co m /page s /page1.html')
except HTTPError as e:      # HTTPError for HTTP status code returned as error
    print(e)
    #
except URLError as e:       # server can't be found (url typo, server down, etc)
    print(e)
    # Note: server is responsible for returning HTTP status code,
    # a missing server can't throw HTTPError
else:
    print('returned html obj successfully')
    # If you return or break in the exception catch, then don't need to use 'else'

    '''
    If no HTTPError or URLError, there's still an issue of unexpected content format,
    eg, check if the tag exists.
    A type None object is returned by type BeautifulSoup object if tag doesn't exist,
    which throws AttributeError when reading data from None.
    '''
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print('Tag anotherTag not found')
    else:
        if badContent == None:
            print('Tag nonExistingTag not found')
        else:
            print('all tags exist')

'''
Combine HTTPError, URLError checks with AttributeError,  = =None checks into a helper function
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getH1(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title if title != None else None


