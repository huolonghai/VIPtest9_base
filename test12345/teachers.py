# encoding = utf-8

import random

# teachers = ['a','b','c','d','e','f','g','h']
# offices = [[],[],[]]
# for name in teachers:
#     num = random.randint(0,2)   # 获取下标
#     offices[num].append(name)   # 将值添加到offices中
# print(offices)
# i = 1

# for i in range(6):
#     for j in range(i,6):
#         print(' ',end='')
#     for k in range(0,i):
#         print('*',end=' ')
#     print()

# 求100以内能被3整除的数，并将作为列表输出
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# for i in a:
#     if i %3 == 0:
#         print(i)
# 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# list_number=[1,2,3,4,5,6,6,7,7,7,8,9]
#
# print(list(set(list_number)))

# 求100以内的质数（只能被1和它本身整除）
# num = []
# for i in range(2,100):
#     j = 2
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         num.append(i)
# print(num)

# 有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
# a = 'aabbbcddef'
# for i in a:
#     if i not in 'abd':
#         print(i)
# 有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
# a = 'welocme to super&Test'
# list = a.split(' ')   # 将a以空格分隔
# print(list)
# new_a = ' '.join(list[::-1])  # 将分隔的单从后面进行重组
# print(new_a)

# 求斐波那契数列 1 1 2 3 5 8 13 ……
n1 = 0
n2 = 1
num = 22
for i in range(1,num):
    if i < 2:
        print(n2,end=' ')
    else:
        n1, n2 = n2, n1 + n2
        print(n2,end=' ')
i = 0
a = 1
b = 1
while i < 24:
    print(a,end=' ')
    a,b = b,a+b
    i += 1