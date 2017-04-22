#!/usr/bin/env python3.5

''' 循环语句 '''

# for...in...
for n in range(1, 5):
    print(n)

# while
index = 0
l = range(1, 20)
while index < 5:
    print(l[index])
    index += 1

# 终止循环
for n in range(1, 4):
    if n == 3: break

# 跳过循环
for n in range(1, 5):
    if n == 3: continue