#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#f = open('/tmp/test.txt', 'r')
#one = f.read(9)
#f.readlines()
#finallseek = f.tell()
#f.seek(9)
#two = f.read(finallseek - 9)
#data = one + "1.1.Jpython\n" + two
#f = open('test.txt', 'w')
#f.write(data)
#f.flush()
#f.close()



'''初始化测试文件'''
# def Cretefile(path, filename, msg):
# 	#清空内存，避免内容重复
# 	f = open(path+filename, 'w')
# 	f.write('')
# 	f.flush()
# 	f.close()
# 	#写入指定内容
# 	f = open(path+filename, 'w')
# 	f.write(msg)
# 	f.flush()
# 	f.close()
# def Catfile(path, filename):
# 	f = open(path+filename, 'r')
# 	print f.readlines()
#
# Text = "1.Python\n2.Java\n3.Ruby"
# i = 1
# fname = 'test' + str(i) + '.txt'
# Cretefile('/tmp/', fname, Text)
# Catfile('/tmp/', fname)




'''指定位置分别插入指定字段实现１ 使用write'''
# f = open('/tmp/test.txt', 'r')
# lins_list = f.readlines()
# stri_list = ['one\n', 'two\n', 'three\n']
# lines = [1, 3, 5]
# #将２个列表转换为一个字典
# dect1 = dict(zip(lines,stri_list))
# #遍历字典把key value 追加到已有列表
# for (i,j) in dect1.items():
# 	lins_list.insert(i, j)
#
# #将列表转换为字符串
# data = ''.join(lins_list)
# f = open('/tmp/test.txt', 'w')
# f.write(data)
# f.flush()
# f.close()
# f = open('/tmp/test.txt', 'r')
# text = f.readlines()
# print text

'''指定位置分别插入指定字段实现２　使用writelines'''

# f = open('/tmp/test1.txt', 'r')
# test1_list = f.readlines()
# num_list = [1, 2, 3]
# stri_list = ['One\n', 'Two\n', 'Three\n']
# items_dict = dict(zip(num_list, stri_list))
# for (i,j) in items_dict.items():
# 	x = i+1
# 	test1_list.insert(i, str(x)+j)
# f.close()
# f = open('/tmp/test1.txt', 'w')
# f.writelines(test1_list)
# f.flush()
# f.close()

'''删除指定行'''
# def DelRow(filename, num):
# 	f = open(filename, 'r')
# 	file_list = f.readlines()
# 	file_list.pop(num)
# 	f = open(filename, 'w')
# 	f.writelines(file_list)
# 	f.flush()
# 	f.close()
#
# DelRow('/tmp/test1.txt', 2)

'''删除匹配行'''
# def DelReRow(filename, remsg):
# 	f = open(filename, 'r')
# 	file_list = f.readlines()
# 	data = []
# 	for line in file_list:
# 		#string.find（）匹配字符串的位置，返回-1代表匹配不到
# 		#string.replace('要替换的字符'，’替换的字符’)
# 		if line.find('remsg') == -1:
# 			data.append(line)
# 	f = open(filename, 'w')
# 	f.writelines(data)
# 	f.flush()
# 	f.close()
#
# DelReRow('/tmp/test1.txt', 'Python')

'''全局替换字符串'''

def ReplaceString(filename, oldstr, newstr):
	f = open(filename, 'r')
	file_list = f.readlines()
	data = []
	for line in file_list:
		#将替换后的string 赋值给ａ，追加ａ到data列表
		a = line.replace(oldstr, newstr)
		data.append(a)
	print data
  	f = open(filename, 'w')
	f.writelines(data)
	f.flush()
 	f.close()

ReplaceString('/tmp/test1.txt', 'Java', 'Prel')

'''处理大文件'''
# 1.遍历读取
# 2.指定字节数读取
