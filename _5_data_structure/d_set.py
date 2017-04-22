#!/usr/bin/env python3.5

''' 集合 '''

# 声明
s = set([1, 2, 3, 3, 4])

# 添加key
s.add(5)
s.add(1)    # 可重复添加，没有效果的

# 删除key
s.remove(1)

# 集合操作
result = s | set([1, 2, 3])
result = s & set([1, 2, 3])

# 元素必须为不可变对象
# set([[1, 2], 1])

print(s)
print(result)