from django.db import models

class Md5s(models.Model):
    passwd = models.CharField(max_length=32)
    hash_md5 = models.CharField(max_length=32)
    hash_md5.editable = False
    passwd.editable = False
    def __unicode__(self):
        return u'%s' % self.passwd
