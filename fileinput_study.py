# -*- coding: utf-8 -*-
import fileinput

# fileinput 模块实现无需修改列表替换字符串
# for  line in fileinput.input(files='/tmp/test.txt', inplace=1, backup=".bak", bufsize=0, mode="r", openhook=None):
#     print line.replace('java', 'perl')

for line in fileinput.input(files='/tmp/test.txt', inplace=1):
    print line
    # print fileinput.filename()
