# -*- coding: UTF-8 -*-
'''
Auto get Best joke from http://www.qiushibaike.com/
'''
import requests
from bs4 import BeautifulSoup
import lxml

#Set default encoding for sysconfig
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#定义joke_num函数，用于获取每个笑话的好笑数集合为一个int list
def joke_num():
    alljoke_list = []
    intjoke_list = []
    #读取前10页的笑话
    for i in range(1, 10):
        url = "http://www.qiushibaike.com/hot/page/%s/?s=4969825" %i
        #requests.get用于获取网页源码，.text 用于把网页源码打印为文本
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        #soup.select选取class=stats-vote的span下的i.number 这部分源码
        jokenum = soup.select("span.stats-vote > i.number")
        #定义一个空列表用于接收变量jokenum源码中的文本到一个列表
        joke_list = []
        #遍历jokenum,.get_text用于筛选文本
        for m in jokenum:
            num = m.get_text()
            joke_list.append(num)
        #将所有循环出来的joke_list汇总到一个列表为alljoke_list
        alljoke_list.extend(joke_list)
    #将alljoke_list中的所有元素从string转换为int类型
    for u in alljoke_list:
        intjoke_list.append(int(u))
    return intjoke_list


#定义函数用于比较一个int类型的list中最大的数字
def mostjoke_num(joke_list):
    m = joke_list[1]
    for i in joke_list:
        if i < m:
            m = m
        elif i > m:
            m = i
    return m

#定义spider,用于爬去糗事百科中的段子，以及每个段子的好笑数
def spider(mostnum):
    for i in range(1, 10):
        url = "http://www.qiushibaike.com/hot/page/%s/?s=4969825" %i
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        text = soup.select("div.content > span")
        joke = soup.select("span.stats-vote > i.number")
        joke_dict = dict(zip(text,joke))
        for (n,m) in joke_dict.items():
            text = n.get_text()
            num = m.get_text()
            intnum = int(num)
            if mostnum == intnum:
                print "最好笑的笑话："
                print text+"\n总共有"+num+"人觉得好笑，你觉得呢?哈哈哈...."
            else:
                continue




spider(mostjoke_num(joke_num()))
