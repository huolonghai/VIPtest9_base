# encoding = utf-8

# lists = [1,2,3,4,5,6,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# print(lists[::-1])
# print(lists.index(5))
# print(lists.count(4))
# print(len(lists))
# lists.append(33)
# print(lists)
# lists.extend('world')
# print(lists)
# lists.insert(2,'hellow')

# a = list(a for a in range(0,100) if a % 3 == 0)
# print(a)

list2 = 'welocme to super&Test'
# a = list2.split(' ')
# i = ' '.join(a)
print(list2[::-1])
# a = [1,2,3,4,5,5,2,3,2,4]
# if i in a:
#     print(1,2,3,4,5)

# user_id = ['jon','tom']
# paw_id = [11,33]
# def add_name():
#     name = str(input('姓名：'))
#     paw = input('密码：')
#     if name in user_id or paw in paw_id :
#         dic = dict(zip(user_id, paw_id))
#         print(f'{name}',dic[name])
#         print('该用户已存在')
#
#     else:
#         user_id.append(name)
#         paw_id.append(paw)
#         dic = dict(zip(user_id,paw_id))
#         print(dic)
#         print('注册成功')
# def selcet_test():
#     name = str(input('姓名：'))
#     if name in user_id:
#         dic = dict(zip(user_id, paw_id))
#         print(f'{name}:',dic[name])
#     else:
#         print('没有该用户')
# def del_test():
#     name = input('姓名：')
#     if name in user_id:
#         dic = dict(zip(user_id, paw_id))
#         dic.pop(str(name))
#         print(dic)
# add_name()
# selcet_test()
# del_test()

a = ['1','2','3']
print(a[:])