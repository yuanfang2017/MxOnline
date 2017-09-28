# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

# 定义course类
class Course(models.Model):
    # 课程名称
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    # 课程描述
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # 课程详情，TextField是不用限制最大长度
    detail = models.TextField(verbose_name=u"课程详情")
    # 课程难易程度
    degree = models.CharField(max_length=30, choices=(("dj", "低级"), ("zj", "中级"), ("gj", "高级")), verbose_name= "难度")
    # 学习时间
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时间")
    # 学习人数
    learn_nums = models.IntegerField(default=0, verbose_name=u"学习人数")
    # 收藏人数
    fas_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    # 课程封面图片
    image = models.ImageField(max_length=100, upload_to='course/%Y/%m', verbose_name=u"课程封面图片")
    # 点击数量
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数量")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    # 通过外键关联Course
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    # 通过外键关联 Lesson
    lesson = models.ForeignKey(Lesson, verbose_name=u"课程", null=True)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    # 通过外键关联Course
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    dowm = models.FileField(max_length=100, upload_to="course/%Y/%m", verbose_name=u"")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
