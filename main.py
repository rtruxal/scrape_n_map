from collections import Counter
import pathlib
import os
import requests
from fake_useragent import UserAgent
from drillbit import Drill
from utils.nonDB_save import basic_file_write, title_to_filename
from utils.soupify_req_quick import html_to_soup





def advanced():
    first_link = 'http://www.httpbin.org'
    ua = UserAgent()
    heads = {'User-Agent': ua.firefox}
    link_counter = Counter()
    s = requests.session()

    soup = Drill.soupify_link(first_link, s, headers=heads)
    link_list = Drill.extract_links_from_soup(soup, link_counter, first_link)
    print(link_counter)



# Works!
def open_n_save(url, root_saving_dir=pathlib.Path(os.path.dirname(__file__), 'data').__str__()):
    soupy, my_session = html_to_soup(url)
    soupy_file_name = title_to_filename(soupy)
    file_pth = os.path.join(root_saving_dir, soupy_file_name) # <- ok for now, gonna need to make dirs for links.
    basic_file_write(soupy.prettify(encoding='UTF-8'), file_pth) # <-don't pass all the soup, it's rude.
    return url, root_saving_dir, soupy, my_session

def step_next(intl_url, curdir, Soup_Object, Session_Object):
    pass

def main():
    url, root_dir, BSoup, Session =  open_n_save('http://testing-ground.scraping.pro')
    print('url: ',url)
    print('root dir: ', root_dir)
    print('Soup Object: ', BSoup)
    print('Request Session: ', Session)


if __name__ == '__main__':
    main()



