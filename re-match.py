#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "This Car are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) (.*)', line, re.M|re.I)

if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
    print(matchObj.group(3))
else:
    print('No match!')