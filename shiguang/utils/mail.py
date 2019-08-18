# 发送邮件激活
import random

from django.core.cache import cache
from django.core.mail import send_mail

from shiguang.settings import EMAIL_HOST_USER


def send_email(email):
    subject = email + '正在进行登录'
    capt = captacha()
    cache.set(email, capt, timeout=180)
    message = '验证码为' + capt

    result = send_mail(subject, message, EMAIL_HOST_USER, [email, ])
    '''
           send_mail()函数： django自带的发送邮件的方法
               subject: 发送的主题
               message: 发送的正文
               EMAIL_HOST_USER: 发送方邮箱地址
               []: 一个列表，表示接收方

            如果成功发送返回1   否则返回0
    '''
    return result


def captacha():
    captacha = random.randint(1000, 9999)
    return str(captacha)
