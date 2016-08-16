import time
import os
import re
import requests
from bs4 import BeautifulSoup
from collections import Counter
from fake_useragent import UserAgent


"""
so far does 3 things:
1 - pretends to be firefox and downloads page
2 - finds links on that page, serves them up as a list
3 - uses a counter to keep track of link redundancy.
    This should prevent dups in returned lists
    and should also notch the counter with key==that link.

"""
class Drill():

    @staticmethod
    def soupify_link(link, req_session, parser='lxml', bs=None, headers=None):
        if headers:
            req = req_session.get(link, headers=headers)
        else:
            req = req_session.get(link)
        if bs:
            bs.clear()
            return bs(req.text, parser)
        return BeautifulSoup(req.text, parser)

    @staticmethod
    def extract_links_from_soup(soup_obj, dict_counter, root_link):
        results = set()
        for link in soup_obj.find_all('a'):
            link_string = str(link.get('href'))
            if link_string.startswith('/'): # <- some of the links are just appenditures of the root link. they all start with /
                full_link = root_link + link_string
                results.add(full_link)
                dict_counter.update({full_link : 1})
            elif link_string.startswith('ht'):
                results.add(link_string)
                dict_counter.update({link_string : 1})
            else:
                dict_counter.update({'shit!' : 1})
        return results


def main():
    first_link = 'http://www.httpbin.org'
    ua = UserAgent()
    heads = {'User-Agent': ua.firefox}
    link_counter = Counter()
    s = requests.session()

    soup = Drill.soupify_link(first_link, s, headers=heads)
    link_list = Drill.extract_links_from_soup(soup, link_counter, first_link)
    print(link_counter)


if __name__ == '__main__':
    main()