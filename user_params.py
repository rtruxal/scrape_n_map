from fake_useragent import UserAgent
from collections import Counter, OrderedDict
from requests import session
from bs4 import BeautifulSoup

class params():
    UA = UserAgent()
    header = {'User-Agent' : UA.firefox.__str__()}
    OD = OrderedDict()
    Cntr = Counter()
    Session = session()
    BS = BeautifulSoup()
