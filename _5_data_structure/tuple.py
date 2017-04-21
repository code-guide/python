#!/usr/bin/env python3.5

''' 元组 '''

# 与列表用法先用，区别是元素不可修改

# 声明 name = (value, value)
students = ('张三', '李四')

# 不可以修改元素
# students[1] = 'asdasd'

# 不可删除单个元素，可以删除整个元组 del name
del students

# 可以连接两个枚举
stu1 = ('张三', '李四')
stu2 = ('王五', )
students = stu1 + stu2

print(students)
