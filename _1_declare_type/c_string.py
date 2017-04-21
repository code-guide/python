#!/usr/bin/env python3.5

''' 字符串 '''

# 表示形式
str = '张三'              # 单引号
str = "北京"              # 双引号
str = '张三是\'好人\''     # 转义字符
str = r'张三是\'好人\''    # 不转义
str = '''line1
多行字符串
line2'''                 # 多行字符串

# 码点
result = ord('张')        # 获取码点
result = chr(24352)      # 解析马甸

# 编码
result = '张三'.encode('utf-8')                           # 字符串 -> 字节型
result = b'\xe5\xbc\xa0\xe4\xb8\x89'.decode('utf-8')     # 字节型 -> 字符串

# 长度
result = len('张三')

# 格式化
result = 'str: %s, int: %d, float: %f, hex: %x' % ('demo', 10, 20.1, 0xac)

print(result)