#coding:utf-8
import requests
import lxml
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://neihanshequ.com/"
html_text = requests.request("GET", url).text
soup = BeautifulSoup(html_text, 'lxml')
duanluo = soup.find_all('div', 'upload-txt')
dianzan_num = soup.find_all('span', 'digg')
dd_dict = dict(zip(duanluo, dianzan_num))
int_num = []
def dianzan_list():
    dianzan_num = soup.find_all('span', 'digg')
    duanluo = soup.find_all('div', 'upload-txt')
    dd_dict = dict(zip(duanluo, dianzan_num))
    for num_text in dianzan_num:
        int_num.append(int(num_text.get_text()))
    int_num.sort()
    int_num.reverse()
    for i in int_num:
        for (n,m) in dd_dict.items():
            int_n = n.get_text()
            int_m = m.get_text()
            if i == int(int_m):
                print "段子的具体是："+int_n+"\n点赞数："+ int_m +"\n"
dianzan_list()
