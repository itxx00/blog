from itxx.blog.models import Config, Papertype, Paper,Link,Comment
from django.contrib import admin

admin.site.register(Config)
admin.site.register(Papertype)
class Paperadmin(admin.ModelAdmin):
    list_display = ['title','papertype','createtime']
    search_fields = ['content']
admin.site.register(Paper,Paperadmin)
class Linkadmin(admin.ModelAdmin):
    list_display = ['linkname','linkaddr']
admin.site.register(Link,Linkadmin)
class Commentadmin(admin.ModelAdmin):
    list_display = ['cid','email','nikename','comment','reply','cmttime']
    search_fields = ['comment']
admin.site.register(Comment,Commentadmin)
