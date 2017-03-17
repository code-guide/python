#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
语句
'''

# 分支
num = 10
if num > 20:
    print('more')
elif num == 20:
    pass
else:
    print('less')

# 循环

# for
sum = 0
for num in range(100):
    sum += num

# while
i = 0
while i < 10:
    i += 1
    if i == 8: break
    if i == 2: continue    
    sum += i
    