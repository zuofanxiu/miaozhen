# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
上述两行指定操作系统执行这个脚本的时候，调用python解释器；
!/usr/bin/env python和!/usr/bin/python区别在于一个通过环境变量去
寻找python解析器，另一个表明python解析器就在/usr/bin/目录下

第二行指定编码格式
'''

# 以下例子为说明单元测试的基本流程

def name_function(firstName, lastName):
    full_name = firstName + ' ' + lastName
    return full_name.title()



