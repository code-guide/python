#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

''' 列表 '''

# 声明 name = [value, value]，不限制类型
students = ['张三', '李四']

# 设置 name[index] = value
students[1] = '王五'
# students[100] = '王五'      越界报错

# 删除 del name[index]
del students[1]
# del students[100]         越界报错

# 长度
result = len(students)

# 重复
students = ['张三'] * 4

# 连接
students += ['李四', '王五']

# 查找
result = '王五' in students

# 遍历
for student in students: print(student)

print(result)
print(students)