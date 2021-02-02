# encoding = utf-8
import os
# f = open('test.txt','w')
# f.write('hello world')
# f = open('test.txt')
# rds = f.readline()
# rd = f.readline()
# print(rd)
# print(rds)
# rd = f.seek(1,2)
# print(rd)
# flag = 1
# dir_name = './'
# file_list = os.listdir(dir_name)
# print(file_list)
# for name in file_list:
#     if flag == 1:
#         new_name = '' + name
#     elif flag == 2:
#         num = len('python-')
#         new_name = name[num:]
#
#     print(new_name)
#     os.rename(dir_name+name,dir_name+new_name)
f = open('python-test.txt')
# f.write('whwhwhwhwh')
ff = f.readlines()
print(ff)

f.close()