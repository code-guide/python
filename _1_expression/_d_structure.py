#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
复合结构
'''

# ========= 列表 list ============

# 声明
persons = ['张三', '李四', '王五']

# 长度
len(persons)            # 3

# 获取元素
persons[0]
persons[-1]
# persons[5]            # error => 越界

# 设置元素
persons[0] = '张三'

# 末尾追加
persons.append('赵六')

# 移除末尾
persons.pop()

# 支持多维，多类型
persons[-1] = ['err', 1]


# ========== 元组 tuple ===========

# 声明:一旦声明就不可以变了
color = ('red', 'yellow', 'blue')


# ========== 字典 dict ============

# 声明
student = { 'name': '张三', 'age': 20 }

# 获取
result = student['name']

# 设置
student['name'] = '李四'

# 校验key
'name' in student
student.get('asdasd')             # None
student.get('asdasd', -1)         # -1

# 删除key
student.pop('age')


# ========== 集合 set =============

# 声明
s = set([1, 2, 3, 1])              # {1, 2, 3}

# 添加元素
s.add(5)

# 删除元素
s.clear(1)

# 集合操作
s & set([1, 2, 3])
s | set([1, 2])