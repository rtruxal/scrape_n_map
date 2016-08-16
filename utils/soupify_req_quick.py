from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

def _soupify_link(link, req_session, parser='lxml', bs=None, headers=None):
    if headers:
        req = req_session.get(link, headers=headers)
    else:
        req = req_session.get(link)
    if bs:
        bs.clear()
        return bs(req.text, parser)
    return BeautifulSoup(req.text, parser)

def html_to_soup(link, user_header=None):
    if not user_header:
        ua = UserAgent()
        heads = {'User-Agent' : ua.firefox}
    else:
        try:
            heads = user_header
        except Exception():
            print('something went wrong w/ header. Using firefox default.')
            ua = UserAgent()
            heads = {'User-Agent' : ua.firefox}
    s = requests.session()
    return _soupify_link(link, s, headers=heads)