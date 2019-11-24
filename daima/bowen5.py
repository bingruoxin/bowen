
# print("你好 中国！")
# print("你好 世界！")
# print("你好 博文！")


'''a = 2
b = 3
print(a+b)'''
# user = 924823387
# password = 111111
# print(user,password)

# name ="小明"
# age = 18
# sex = True
# hight = 1.75
# weinht = 75
# a = int(input("请输入单价："))
# a = 25
# b = 10
# print("%d元，%f" % (a,b))
# name = str(input("输入你的名字:"))
# student_no = int(input("输入你的学号："))
# print("我的名字叫 %s,请多多关照,输出:%06d" % (name,student_no))
# price = float(input("输入价格："))
# weight = float(input("重量:"))
# money = price*weight
# print("苹果单价:%.02f,重量:%.02f,money:%.02f" % (price,weight,money))
# scale = float(input("数据比例是："))
# print("%0.2f%%" % scale)
# age = int(input("年龄"))
# if age>=18:
#     print("去找女朋友!")
# else:
#     print("回家写作业去吧！")
# age =int(input("输入年龄："))
# if age> 0 and age < 120:
#     print("你好")
# else:
#     print("不好")
# python_score = int(input("输入python成绩"))
# c_score = int(input("输入c成绩"))
# if python_score > 60 or c_score >60:
#     print("合格")
# else:
#     print("不合格")
# fenshu = int(input("输入分数："))
# if fenshu > 0 and fenshu < 60:
#     print("不及格")
# elif fenshu >=60 and fenshu < 70:
#     print("及格")
# elif fenshu >=70 and fenshu < 90:
#    print("一般")
# elif fenshu >=90 and fenshu <=100:
#     print("优秀")
# else:
#     print("请重新输入")
# a = int(input("输入"))
# if a % 2 == 0:
#     if a % 3 == 0:
#         print("hello world")
# a = 1
# b = 2
# a += b
# print(a)
# while 1 :
#     a = int(input("输入："))
#     b = 1
#     if a == 1 and b == 1:
#             print("平局")
#     elif a == 2 and b == 1:
#             print("b,赢")
#     elif a == 3 and b == 1:
#          print("a,赢")
# import random
# a = int(input("输入:"))
# b =
# if (a == 3 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 3):
#     print("玩家赢")
# elif a == b:
#     print("平局")
# else:
#     print("电脑赢")
# a = int(input("请出示车票:"))
# if a == 1:
# # 是否有票 1 代表有票 ，
#     print("请通过安检")
#     b = int(input("刀的长度:"))
# # 刀有多长，大于20 不允许上车
#     if b >= 20:
#         print("不允许上车 %d" % b)
# else:
#     print("请买车票")
# 如果没票 请买票
# a = [30,28,77,16,98]
# for i in range(len(a) - 1):
#     for b in range(len(a)-1):
#         if a[b] < a[b + 1]:
#             a[b],a[b+1] = a[b+1],a[b]
# print(a)
# print(len(a))
# a = [30,28,77,16,98]
# for i in range(len(a) - 1):
#     for b in range(i+1,len(a)):
#         if a[i] < a[b]:
#             a[i],a[b] = a[b],a[i]
# print(a)
# print(len(a))

# 输出1~100偶数和

# b = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         b += i
# print(b)


#!/usr/bin/python
# -*-coding:utf8-*-
from time import *
import smtplib
#负责构建文本
from email.mime.image import MIMEImage
#负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
#负责构建文本
from email.mime.text import MIMEText
'''2，设置邮箱域名，发件人邮箱，收件人邮箱，
发件人授权码'''
# for i in range(10):
#设置邮箱域名，smtp服务器，这里使用的163邮箱
mail_host = 'smtp.163.com'
#发件人邮箱
mail_sender = 'zhangbiao9937@163.com'
#邮箱授权码。注意这里不是邮箱密码 licence:许可证
mail_licence = 'zwxywy242698'
#收件人邮箱，可以为多个收件人
mail_receivers ='1904107684@qq.com'

'''3,创建一个空邮箱，这里面可以添加文本，图片，附件'''
message = MIMEMultipart()

'''4,设置邮件头部内容'''
#设置邮件主题
message['subject'] = '这是我测试的第一封邮件'
#设置发送者
message['from'] = mail_sender
#设置邮件接收者
message['to'] = str(mail_receivers)

'''5，添加正文文本'''
#邮件正文内容
text = '你个小狗,xiaoxiaogou'
#处理文本
info_text = MIMEText(text)
#向MIMEMultipart对象中添加文本对象
message.attach(info_text)

'''6,添加图片'''
#使用open读取图片
image_data= open(r'C:\Users\biao\Desktop\图片\长发初音未来公主殿下 miku 抱着书本 4k竖屏手机壁纸_彼岸图网.jpg','rb')
#处理图片
info_image = MIMEImage(image_data.read())
#关闭打开的图片文件
image_data.close()
#添加图片文件到邮件信息当中去
message.attach(info_image)

''',发送邮件'''
#创建smtp对象,设置发件人邮箱的域名和端口，端口地址为25
stp = smtplib.SMTP_SSL(mail_host,465)

#登录邮箱
stp.login(mail_sender,mail_licence)
#发送邮件,修改数据类型
stp.sendmail(mail_sender,mail_receivers,message.as_string())
print('邮件发送成功')
#关闭smtp对象
stp.close()
    # sleep(60)

