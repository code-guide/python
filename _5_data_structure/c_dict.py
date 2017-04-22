#!/usr/bin/env python3.5

''' 字典 '''

# 声明 name = {key: value}
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 修改 name[key] = value
result = dic['a']
dic['a'] = 2
# dic['asdas']      访问不存在的key会报错

# 判断key是否存在
result = 'c' in dic
result = dic.get('q', 'empty return value')

# 删除
del dic['b']
dic.pop('c')
# del dic

# 遍历
for key in dic: print('%s: %s' % (key, dic[key]))

print(result)
print(dic)