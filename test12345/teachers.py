# encoding = utf-8

# class mao():
#     def yu(self):
#         print('小猫爱吃鱼')
#     def shui(self):
#         print('小猫要喝水')
# m = mao()
# m.yu()
# m.shui()

# class ning():
#     def __init__(self,zhong):
#         self.zhong = zhong
#     def pao(self):
#         a = self.zhong - 0.5
#         print(a)
#     def chi(self):
#         c = self.zhong + 1
#         print(c)
# class mei(ning):
#     pass
# n = ning(75)
# m = mei(45)
# m.pao()
# m.chi()

# -*- coding utf-8 -*-


# class washer():
#     def __init__(self):
#         self.wedth = 500
#         self.height = 800
#     def print_info(self):
#         print(f'洗衣机的宽度:{self.wedth},洗衣机的高度:{self.height}')
#
# haier = washer()
# haier.print_info()

# class washer():
#     def __init__(self,wedth,height):
#         self.wedth = wedth
#         self.height = height
#     def print_info(self):
#         print(f'洗衣机的宽度:{self.wedth},洗衣机的高度:{self.height}')
#     def __str__(self):
#         return '这是洗衣机的说明书'
# haier = washer(510,820)
# haier.print_info()
# print(haier)

# class washer():
#     def print_info(self):
#         print(f'洗衣机的宽度:{self.wedth},洗衣机的高度:{self.height}')
# haier = washer()
# haier.wedth = 540
# haier.height = 840
# haier.print_info()

# __str__()#####
# class washer():
#     def __init__(self,wedth,height):
#         self.wedth = wedth
#         self.height = height
#     def __str__(self):
#         return '这是海尔的说明书'
# haier = washer(410,601)
# print(haier)

###  烤地瓜  ###
# class SweetPotato():
#     def __init__(self):
#         self.cook_time = 0  # 被烤地瓜时间
#         self.cook_static = '生的'  # 地瓜状态
#         self.condiments = []   # 调料列表
#     def cook(self,time):
#         self.cook_time += time
#         if 0 <= self.cook_time < 3:   # 时间大于0，小于3分钟的状态
#             self.cook_static = '生的，不能吃'
#         elif 3 <= self.cook_time < 5: # 时间大于3分钟，小于5分钟的状态
#             self.cook_static = '半生不熟，再等会儿'
#         elif 5 <= self.cook_time < 8: # 时间大于5分钟，小于8分钟的状态
#             self.cook_static = '熟了，可以吃了'
#         elif self.cook_time > 8:  # 时间大于8分钟的状态
#             self.cook_static = '烤糊了'
#
#     def add_condiments(self,condiment):
#
#             self.condiments.append(condiment)
#
#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static},添加的调料有{self.condiments}'
# digua = SweetPotato()
# digua.cook(1)
# digua.add_condiments('油')
# print(digua)
# digua.cook(2)
# digua.add_condiments('酱油')
# print(digua)
# digua.cook(2)
# digua.add_condiments('辣椒面')
# print(digua)
# digua.cook(4)
# digua.add_condiments('胡椒粉')
# print(digua)

######搬家具#####

# class Furniture():
#     def __init__(self,name,area):
#         self.name = name  # 家具名称
#         self.area = area    # 家具占地面积
# class Home():
#     def __init__(self,address,area):
#         self.address = address      # 家地址
#         self.area = area    # 房屋面积
#         self.free_area = area   # 剩余面积
#         self.furniture = []     # 家具列表
#
#     def add_furniture(self,item):
#         if self.free_area >= item.area:     # 判断剩余面积大于家具面积
#             # self.furniture.append()
#             self.furniture.append(item.name)    # 添加家具名称到列表里
#             self.furniture.append(item.area)    # 添加家具占地面积到列表里
#             self.free_area -= item.area    # 剩余面积= 剩余面积-家具占地面积
#         else:
#             print('没地方了')
#     def __str__(self):
#         return f'你家住{self.address},房屋面积是{self.area},放置家具剩余面积是{self.free_area}，放置的家具名称和占地面积是{self.furniture}'
# bed = Furniture('床',9)
# jia = Home('北京',200)
#
# jia.add_furniture(bed)
# print(jia)
# shafa = Furniture('沙发',20)
# jia.add_furniture(shafa)
# print(jia)
#
# feiji = Furniture('飞机',300)
# jia.add_furniture(feiji)
# print(jia)

class Gun():
    def __init__(self,name,launch):
        self.name = name
        self.launch = launch   # 发射的子弹
class soldiers():
    def __init__(self,name,gun_name,remaining):   # 士兵，枪名，子弹剩余数量
        self.name = name
        self.gun_name = gun_name
        self.capacity = remaining
        self.remaining = remaining
        self.add_count = remaining
    def fire_test(self,item):
        if self.remaining >= item.launch:    # 剩余子弹>=发射的子弹
            self.remaining -= item.launch
        else:
            print('请装填子弹')
    def add_bullet(self):
        bullet = self.remaining - a.launch
        if bullet == 0:
            a.launch += bullet
        else:
            print('还有子弹')
    def __str__(self):
        return f'士兵{self.name }的{self.gun_name}弹夹容量是{self.capacity}发子弹，射出{a.launch}发子弹,剩余数量{self.remaining}发，打完后添加{a.launch}发子弹'
a = Gun('AK47',30)
f = soldiers('瑞恩','AK47',50)
f.fire_test(a)
print(f)
a = Gun('AK47',20)
f.fire_test(a)
print(f)