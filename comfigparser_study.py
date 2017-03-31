# -*- coding: utf-8 -*-
from configparser import ConfigParser

#查找对应key value
# conf = ConfigParser()
# conf.read('conf.ini')
# section = conf.sections()[1]
# option = conf.options(section)
# for key in option:
#     if key == 'host':
#         #给出key 反查索引
#         index = option.index('host')
#         value = conf.get(section,option[index])
#         print key, value

#更新或添加key value
# conf_file = ConfigParser()
# conf_file.read('conf.ini')
# cf = open('conf.ini', 'w')
# conf_file.set('host1', 'port', '2222')
# conf_file.write(cf)

#添加一组配置
# conf = ConfigParser()
# conf.read('conf.ini')
# cf = open('conf.ini', 'w')
# conf.add_section('host4')
# conf.set('host4', 'host', '192.168.100.222')
# conf.set('host4', 'port', '9988')
# conf.set('host4', 'user', 'root')
# conf.set('host4', 'pass', '12345')
# conf.write(cf)

conf = ConfigParser()
conf.read('conf.ini')
cf = open('conf.ini', 'w')
conf.remove_section('host4')
conf.remove_option('host3', 'pass')
conf.write(cf)
