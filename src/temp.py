import re

['section', '.data']

['numArray', 'times', 64, 'db', 1]

['msgVal', 'db', '"Value:', '"']
['lenmsgVal', 'equ', '$-msgVal']

['msgRes', 'db', '"Result', 'of', 'array', 'addition', 'is:', '"']
['lenmsgRes', 'equ', '$-msgRes']

['count', 'db', 5]
l1 = (['temp1', 'd', 0])

str1 = str()
for ele in l1:
    str1 += str(ele)

print(str1)

print(re.findall('db|dw|dd|dq', str1))