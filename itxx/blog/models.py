#coding:utf-8
from django.db import models
from datetime import datetime

# Create your models here.
class Config(models.Model):
    name = models.CharField(max_length=30,unique=False,verbose_name="博客名称")
    address = models.CharField(max_length=30,verbose_name="博客域名")
    email = models.EmailField()
    online = models.NullBooleanField(verbose_name="是否开启")
    about = models.TextField(max_length=3000,verbose_name="关于信息")
    def __unicode__(self):
        return self.name

class Papertype(models.Model):
    typename = models.CharField(max_length=20)
    orderby = models.IntegerField()
    def __unicode__(self):
        return self.typename

class Paper(models.Model):
    title = models.CharField(max_length=60,verbose_name="文章标题")
    papertype = models.ForeignKey(Papertype,verbose_name="文章分类")
    createtime = models.DateTimeField(default=datetime.now(),verbose_name="撰写时间", auto_now_add=True)
    class Meta:
        get_latest_by = 'createtime'

    content = models.TextField(max_length=30000,verbose_name="文章内容")
    degree = models.IntegerField(blank=True,null=True,verbose_name="浏览次数")
    degree.editable = False
    def __unicode__(self):
        return self.title

class Link(models.Model):
    linkname = models.CharField(max_length=30,verbose_name="链接名称")
    linkaddr = models.URLField(verbose_name="链接地址")
    def __unicode__(self):
        return self.linkname

class Comment(models.Model):
    cid = models.ForeignKey(Paper,verbose_name="文章标题")
    email = models.EmailField(verbose_name="访客email")
    nikename = models.CharField(max_length=30,verbose_name="访客昵称")
    cmttime = models.DateTimeField(default=datetime.now(),verbose_name="评论时间")
    comment = models.CharField(max_length=100,verbose_name="评论内容")
    reply = models.CharField(max_length=300,verbose_name="回复")
    #mailreply = models.NullBooleanField(verbose_name = "是否发送邮件通知")
    def __unicode__(self):
        return self.email