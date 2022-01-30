# -*- coding: utf-8 -*-
# noinspection LongLine
"""
Scrapy
------
Scrapy is an application framework for crawling
web sites and extracting structured data which
can be used for a wide range of useful applications,
like data mining, information processing or
historical archival.

Here's an example copied from the official
scrapy documentation; "Scrapy at a glance", that
crawls a simplified pagination page of quotes with
meta-data tags categorizing the quotes.

Source:https://docs.scrapy.org/en/latest/intro/overview.html#walk-through-of-an-example-spider


The example is annotated by the author (omgitskuei)
for the purpose of being a 'quick look' reference into
what makes up a scrapy web crawler.


Created on Sun Oct 24 19:39:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    """
    Here’s the code for a spider that scrapes
    famous quotes from website http://quotes.toscrape.com,
    following the pagination
    """

    name = 'quotes'

    # The crawl started by making requests to the URLs defined
    # in the start_urls attribute (only the URL for quotes in
    # humor category).
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    # called the default callback method parse, passing the
    # response object as an argument.
    def parse(self, response):
        print('running parse(self, response)')

        count = 0
        # loop through the quote elements using a CSS Selector
        for quote in response.css('div.quote'):
            # yield a Python dict with the extracted quote text and author
            each_match = {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get()
            }
            count = count+1
            print('#' + count)
            yield each_match

        # look for a link to the next page and schedule another request
        # using the same parse method as callback.
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        # NOTE: ^ One of the main advantages about Scrapy: requests are
        # scheduled and processed asynchronously.
