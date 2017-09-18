# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    # 昵称
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称", default=u"")
    # 生日
    birth_date =models.DateField(max_length=100, verbose_name=u"生日", null=True, blank=True)
    # 性别
    gender = models.CharField(max_length=5, choices=(("male", u"男"), ("female", u"女")), default="female")
    # 区域
    address = models.CharField(max_length=100, verbose_name=u"区域", default=u"")
    # 手机号
    mobie = models.CharField(max_length=11, verbose_name=u"手机号", null=True,blank=True)
    # 用户图像
    image = models.ImageField(max_length=100, upload_to="image/%Y/%M", default=u"image/default.png")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载Unicode方法，如果没有重载，那么在实例化UserProfile的时候将不能答应我们自定义的字符串
    def __unicode__(self):
        return self.username


# 定义邮箱验证码的类
class EmailVerifyCode(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 邮箱
    email = models.CharField(max_length=50, verbose_name=u"邮箱")
    # 发送方式，找回密码or注册
    send_type = models.CharField(max_length=10, choices=(("register", u"注册"), ("forget", u"找回密码")))
    # 发送时间
    send_time = models.DateTimeField(max_length=50, default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


# 轮播图的类
class Banner(models.Model):
    # 标题
    title = models.CharField(max_length=100, verbose_name=u"标题")
    # 轮播图片
    image = models.ImageField(max_length=100, verbose_name=u"轮播图片", upload_to="banner/%Y/%M")
    # 跳转地址
    url = models.URLField(max_length=100, verbose_name=u"跳转地址")
    # 轮播顺序
    index = models.IntegerField(max_length=100, verbose_name=u"轮播顺序")
    # 添加时间
    add_time = models.DateTimeField(max_length=100, verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name




