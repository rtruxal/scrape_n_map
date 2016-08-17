from collections import Counter
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




def basics(url, root_saving_dir=os.getcwd()):
    soupy = html_to_soup(url)
    soupy_file_name = title_to_filename(soupy)
    file_pth = os.path.join(root_saving_dir, soupy_file_name)
    # print(soupy.prettify().find('\n'))
    # print(type(soupy.prettify().split('\n')))
    ## LOOK AT THIS IT IS BROKEN.
    basic_file_write(soupy.prettify(encoding='UTF-8'), file_pth)



if __name__ == '__main__':
    basics('http://testing-ground.scraping.pro')