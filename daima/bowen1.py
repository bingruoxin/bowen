#!/usr/bin/python
# -*-coding:utf8-*-
# b = input('请输入：')
# if "a" in b:
#     print(123)
# else:
#     print(456)
# b = input('请输入：')
# if "a" == b:
#     print(123)
# else:
#     print(456)
# while 1:
#     i = (input("输入5个字符："))
#     if i[0] == '1' or i[-1] == '3':
#         print(type(i))
# a ='asdfqb'
# print(a[::-2])
# a = 0
# i = 0
# if i < 100:
#     a += i
#     i += 1
# print(a)
# while 1:
#     i = input("输入：")
#     if ('a' and 'b') in i:
#         print("123")
#     elif 'a' in i:
#         print("456")
#     elif 'b' in i:
#         print("789")
#     else:
#         print("没了")
# while 1:
#     i = int(input("输入："))
#     if i < 100:
#         if i < 90:
#             if i< 70:
#                 if i < 60:
#                     if i < 0:
#                         print("请重新输入")
#                     else:
#                         print("不及格")
#                 else:
#                     print("及格")
#             else:
#                 print("一般")
#         else:
#             print("优秀")
#     else:
#         print("请重新输入")
# i = int(input("请输入等级："))
# if i >= 0 and i <= 2:
#     print("生")
# elif i >= 3 and i <= 4:
#     print("半生不熟")
# elif i >= 5 and i <= 8:
#     print("熟的")
# else:
#     print("焦了")
# a= 'edf'.upper()
# print(a)
# print(input("shuru:").lower)
# a = ['452','4525']
# b = '分隔符'.join(a)
# print(b)
# i = 1
# while i <= 9:
#     b = 1
#     while b <= i:
#         a = '{}×{}={}'.format(b,i,b*i)
#         b += 1
#         print(a,end="\t")
#     i += 1
#     print("")
# b = 'asadafad'
# print(b)
# c = 0
# for i in range(0,101,):
#     if i%2 == 0:
#         print()
#     else:
#         c += i
# print(c)
# i = 1
# for i in :
#     if i < 100:
#         break
# else:
#     print(a)
# a = ['abc','ABc','abb','cda']
# for i in a:
#     if (a[i].startswith('a') or a[i].startswith('A') )and a[i].endswith('c'):
#         print(a[i])
# b = [11,22,33,44,55,66,77,88,99]
# d = []
# f = []
# for i in b:
#     if i <= 55:
#         d.append(i)
#     else:
#         i > 55
#         f.append(i)
# print(d,f)
# while 1:
#     a = input("请输入：")
#     for i in a:
#         b = a.replace(" ","")
#         c = b.title()
#         d = c.replace( 'a',"123")
#     print(d)
# a = [12,12,12,34,235,34,34]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a = [123,123,123,234,234,234,345]
# # print("出现的次数:%d,%d,%d" % (a.count(123),a.count(234),a.count(345)))
# for i in a:
#     for i in a:
#         if a.count(i) >1:
#             a.remove(i)
# print(a)
# import random
# a = random.randint(0,1)
# i = 0
# for i in range(3):
#     b = int(input("请输入:"))
#     if a > b:
#         print("小了")
#            print("小了")
#     if a < b:
#         print("大了")
#            print("大了")
#     if a == b:
#         print("恭喜")
#         break
# else:
#     print("废物")
# a = 'user'
# for i in range(51):
#     print("%s%d" % (a,i))
# i = input("请输入:")
# for a in range(len(i)):
#     if i[a] > i[a+1]:
#         i[a],i[a+1] = i[a+1],i[a]
#         print(a)


# a = '{} {}'.format(123,123)
# print(type(a))
# a = 'asdxdfwsdfwdas'.split('d')
# b = ('d').join(a)
# c = b.startswith('c')
# print(a)
# print(b)
# print(c)
# a = [11,22,33,66,77,88]
# b = {'key1':[],'key2':[]}
# for i in a:
#     if i < 66:
#         b['key1'].append(i)
#     else:
#         b['key2'].append(i)
# print(b)


#
# dict = {'key1':'alex','key2':' aric','key3':'Alex','key4':'Tony'}
# b = list(dict.values())
# for i in b:
#     c = i.replace(' ','')
#     if (c.startswith('a') or i.startswith('A')) and (c.endswith('c')):
#         print(c)

# a =16
# for i in range(1,101,2):
#     if i%3 == 0 or i%5 == 0 or i%7 == 0:
#         pass
#     else:
#         a += i
# print(a)


# li = ['手机','电脑','鼠标垫','游艇']
# for i,r in enumerate(li):
#     print(i,r)
# a = int(input('请输入:'))
# print(li[a])


# li = [1,2,3,'a',4,'c']
# dict = {}
# for i in range(1,len(li),2):
#     if 'k1' in dict.keys():
#         if type(dict['k1']) == list:
#             dict['k1'].append(li[i])
#     else:
#         dict['k1'] = []
#         dict['k1'].append(li[i])
# print(dict)

# a = input('请输入:')
# b = []
# f = {}
# d = []
# for i in range(len(a)):
#     f[a[i]] = (a.count(a[i]))
# for r,w in f.items():
#     d.append(r)
#     b.append(w)
# for c in range(len(b)-1):
#     for c in range(len(b)-1):
#         if b[c] < b[c+1]:
#             b[c],b[c+1] = b[c+1],b[c]
#             d[c],d[c+1] = d[c+1],d[c]
# print(f)
#    print(c)
# x =''.join(d)
# print(x)
# print(b)
# print(a[i])
# print(b)
# print(f)


# for i in range(2,101):
#     a = 0
#     for b in range(1,i):
#         if i%b == 0:
#             a += b
#     if a == i:
#         print(a)

# def ss():
# #     global a
# #     a = 2
# #     print(a)
# # ss()
# # print(a)



# def sum1(x = 2,y = 100):
#     a = 0
#     for i in range(x,y+1):
#         b = [j for j in range(2,i) if i%j == 0]
#         if len(b) == 0:
#             a += i
#     print(a)
# def hsm(**kwargs):
#     print(kwargs)
# hsm(a=123,s=13,d='we',f='ygv')
# def 函数名():
#     执行语句块
#     return 数据

# def lei(a,b):
#     for i in range(len(a)):
#         for c in range(i+1,len(a)):
#             if a[i] + a[c] == b:
#                 print(a[i],a[c])
#     print(type(a))
# lei([12,2,1,10,6,7,3],13)

# # 购物车
# q = int(input("资产:"))
# w = {0:'电脑',1:'鼠标',2:'p30',3:'源计划'}
# e = {'电脑':19,'鼠标':10,'p30':30,'源计划':23}
# print(w)
# t = {}
# z = []
# def sp():
#     while 1:
#         r = int(input("编号:"))
#         if r < len(w):
#             t[w[r]] = e[w[r]]
#             # print(a)
#             print(t)
#         else:
#             print("未知编号")
#             break
# sp()
# print(t)
# a =list((t.values()))
# print(a)
# while 1:
#     if sum(a) > q:
#         print("账户余额不足")
#         s = int(input("充值(1)或移除购物车:"))
#         if s == 1:
#             q += int(input("充值金额:"))
#         else:
#             d = input("移除商品名:")
#             f = t.pop(d)
#             a = list(t.values())
#     else:
#         print("购买成功")
#         break



