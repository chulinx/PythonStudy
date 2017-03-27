import sys
from ConfigParser import ConfigParser

configfile = 'conf.ini'
conf = ConfigParser()
conf.read(configfile)
#@ section= raw_input('Input your want to seclet section: ')
# section = sys.argv[1]
# option = sys.argv[2]
# value = conf.get(section, option, )
# print option+': '+value
section = conf.sections()
for section in section:
    print "----------------------"
    option =conf.options(section)
    for option in option:
        key = conf.get(section, option)
        print option+': '+key
    print "----------------------\n"
