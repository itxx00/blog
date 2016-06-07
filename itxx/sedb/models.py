#coding:utf-8
from django.db import models

class People(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    email = models.EmailField()
    idcard = models.CharField(max_length=18)
    address = models.CharField(max_length=40)
    company = models.CharField(max_length=30)
    counttype = models.CharField(max_length=10)
    count = models.CharField(max_length=32)
    passtype = models.CharField(max_length=5)
    password = models.CharField(max_length=40)
#    image = models.ImageField(upload_to='/upload/')
#    ipaddr = models.IPAddressField()
    def __unicode__(self):
        return '%s' % (self.nickname)
    name.verbose_name = '姓名'
    nickname.verbose_name = '网名'
    email.verbose_name = '邮箱'
    idcard.verbose_name = '身份证'
    address.verbose_name = '住址'
    company.verbose_name = '公司'
    counttype.verbose_name = '帐号类型'
    count.verbose_name = '帐号'
    passtype.verbose_name = '密码类型'
    password.verbose_name = '密码'
