# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserProfile
from course.models import Course

# Create your models here.


# 用户我要学习的那个提交表单
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=20, verbose_name=u"手机号")
    course_name = models.CharField(max_length=20, verbose_name=u"要学习课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


# 课程评价
class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"评价姓名")
    course = models.ForeignKey(Course, verbose_name=u"评价课程")
    comments = models.CharField(max_length=200, verbose_name=u"评价")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评价时间")

    class Meta:
        verbose_name = u"课程评价"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    fav_type = models.CharField(choices=(("1", "课程收藏"), ("2", "机构收藏"), ("3", "讲师收藏")), default=1, verbose_name=u"收藏")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

