#!/usr/bin/python
# -*-coding:utf8-*-

# high = int(input("井深:"))
# up = int(input("上爬:"))
# down = int(input("下滑:"))
# a = 0
# b = 0
# i = 1
# while i >= 0:
#     if up >= high:
#         print("%d天" % (i))
#         break
#     elif up - down <= 0:
#         print("爬不出来")
#         break
#     elif b >= high:
#         print("%d天" % (i))
#         break
#     else:
#         a += (up - down)
#         i += 1
#         b = a + up

# n = 1
# s = 0
# k = int(input("输入(1-15):"))
# while n > 0:
#     s += 1/n
#     if s > k:
#        print(n)
#        break
#     else:
#         n += 1


# i = int(input("费用:"))
# n = int(input("人数:"))
# for x in range(i//3):
#     for y in range(i//2):
#         if 2*x + y +n == i:
#             print("%d %d %d" % (x,y,n - x - y))



# try:
#     int('aadf')
#     print('aaa')
# except ValueError:
#     print("类型错误")
# else:
#     print("结束")
# finally:
#     print("asdf")

# try :
#     raise ValueError
# except ValueError as f:
#     print("值异常")
#     print(f)