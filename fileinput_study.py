# -*- coding utf-8 -*-
import fileinput
for line in fileinput.input('/tmp/test.txt'):
    print line + '\tRead Row nums\t'+ str(fileinput.lineno())+'\tRead Row num\t'+str(fileinput.filelineno())+'\tFileName\t'+fileinput.filename()
#执行结果
# 1.Python
# 	Read Row nums	1	Read Row num	1	FileName	/tmp/test.txt
# one
# 	Read Row nums	2	Read Row num	2	FileName	/tmp/test.txt
# one
# 	Read Row nums	3	Read Row num	3	FileName	/tmp/test.txt
# two
# 	Read Row nums	4	Read Row num	4	FileName	/tmp/test.txt
# one
# 	Read Row nums	5	Read Row num	5	FileName	/tmp/test.txt
# three
# 	Read Row nums	6	Read Row num	6	FileName	/tmp/test.txt
# two
# 	Read Row nums	7	Read Row num	7	FileName	/tmp/test.txt
# one
# 	Read Row nums	8	Read Row num	8	FileName	/tmp/test.txt
# three
# 	Read Row nums	9	Read Row num	9	FileName	/tmp/test.txt
# two
# 	Read Row nums	10	Read Row num	10	FileName	/tmp/test.txt
# one
# 	Read Row nums	11	Read Row num	11	FileName	/tmp/test.txt
# three
# 	Read Row nums	12	Read Row num	12	FileName	/tmp/test.txt
# two
# 	Read Row nums	13	Read Row num	13	FileName	/tmp/test.txt
# 2.Java
# 	Read Row nums	14	Read Row num	14	FileName	/tmp/test.txt
# three
# 	Read Row nums	15	Read Row num	15	FileName	/tmp/test.txt
# two
# 	Read Row nums	16	Read Row num	16	FileName	/tmp/test.txt
# 3.Ruby
# 	Read Row nums	17	Read Row num	17	FileName	/tmp/test.txt
# three
# 	Read Row nums	18	Read Row num	18	FileName	/tmp/test.txt
