#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# 上面的注释指定编码
'''
字符串 不可变对象
'''

# 声明
str = "demo"            # 双引号
str = 'demo'            # 单引号
str = 'demo \n'         # 转义字符
str = r'demo \n'        # 不转义
str = '''demo
demo
'''                     # 多行文本

# 码点
c = "C"
result = ord(c)         # 67
result = chr(result)    # C

# 支持utf-8
c = "中"
result = ord(c)         # 20013
result = chr(result)    # 中

# str => bytes
result = b'demo'                    # 只适用ASCII
result = '中国'.encode('utf-8')      # 适用于unicode等所有

# bytes => str
result.decode('utf-8')           

# 计算长度
l = len(result)

# 格式化字符串
result = '''
    name: %s(string);
    age: %d(int);
    price: %f(float);
    ox: %x(hexadecimal);
    转义：%%
''' % ('张三', 20, 2.1, 0x12)

print(result)