# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


# 城市类
class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    desc = models.CharField(max_length=200, verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击次数")
    # 收藏人数
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(max_length=100, upload_to="org/%Y/%m", verbose_name=u"机构封面图片")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(City, verbose_name=u"机构所在的城市")

    class Meta:
        verbose_name = u"教学机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"教师姓名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"工作岗位")
    points = models.CharField(max_length=50, verbose_name=u"教学特色")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
