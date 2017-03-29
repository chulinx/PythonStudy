#coding:utf-8
import urllib, urllib2, re

def spaid():
    for i in range(1, 10):
        url = "http://www.qiushibaike.com/8hr/page/%s/?s=4969293" % i
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        Request = urllib2.Request(url,headers=headers)
        html = urllib2.urlopen(Request)
        source = html.read()
        return source

def rep(text):
    joke = re.findall(r"<span>(.*?)<br/>(.*?)</span>", text)
    try:
        for i in range(0, 50):
            print joke[i][0]+joke[i][1]+"\n"
    except Exception as e:
        print e
def most(text):
    mosts = re.findall(r'<i class="number">\d{1,10}</i>', text)
    for i in mosts:
        num = re.findall(r'\d{1,10}',i )
        print num


print rep(spaid()),most(spaid())
