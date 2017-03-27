# -*- coding: utf-8 -*-
import sys
import os
import random
import platform
from ConfigParser import ConfigParser
# #sys.argv
# print sys.argv[0]
# print sys.argv[1]
# print sys.argv[2]
# print sys.argv[3]
# print sys.argv
# print len(sys.argv)
#
# # 执行结果
# # python PythonOneselfMoudel.py a b c
# # PythonOneselfMoudel.py
# # a
# # b
# # c
# # ['PythonOneselfMoudel.py', 'a', 'b', 'c']
# # 4
#
# print sys.version() # 打印系统类型
# print sys.path() #获取系统模块路径 打印一个列表
# print sys.version #打印python版本

#os模块

#random
# random.randint(a, b) #返回a b之间的一个整数
# random.random()  #随机返回0-1之间的随机数
# random.randrange(start, stop, 跳数) #返回整数范围的随机整数，可设置跳数
# random.sample(population, k) #从一个列表返回k个元素
# random.choice(seq) #从一个列表中返回一个元素


# #platform
# platform_list = [platform.platform(),
#                 platform.processor(),
#                 platform.system(),
#                 platform.uname(),
#                 platform.version(),
#                 platform.node(),
#                 platform.python_version(),
#                 platform.machine()
#                 ]
#
# num = range(len(platform_list))
# platform_dict = dict(zip(num, platform_list))
# for (i, j) in platform_dict.items():
#     print i, j

#ConfigParser模块

#conf.ini
# [host1]                 #标识
# host = 192.168.1.1      # host port user pass 键
# port = 22               # 192.168.1.1 22 zhangsan 123 值
# user = zhangsan         # 配置文件读取思路：
# pass = 123              # 先用方法read读取配置文件 再section选取标识 再根据标识用option选取键，再get根据键和标识选取值

#从配置文件中筛选想要的值
# conf = ConfigParser()
# conf.read('conf.ini')
# section = conf.sections()[0]
# option = conf.options(section)
# ip = '172.17.0.1'
# for key in option:
#     if key == 'port':
#         value = conf.get(section, key)
#         print 'ssh '+ip+':'+value

# 打印所有key：value
# conf = ConfigParser()
# conf.read('conf.ini')
# section = conf.sections()
# for section in section:
#     option = conf.options(section)
#     for option in option:
#         print option + ':' + conf.get(section, option)

#更新value
# conf = ConfigParser()
# conf.read('conf.ini')
# cf = open('conf.ini', 'w')
# conf.set('host1', 'port', value=2222)
# conf.write(cf)

#添加选项
# conf = ConfigParser()
# conf.read('conf.ini')
# cf = open('conf.ini', 'w')
# conf.add_section('host4')
# conf.set('host4', 'host', value='192.168.22.78')
# conf.set('host4', 'port', value=2223)
# conf.set('host4', 'user', 'root')
# conf.set('host4', 'pass', '12345')
# conf.write(cf)
