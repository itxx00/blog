from itxx.search.models import Md5s
from django.contrib import admin

class Md5Admin(admin.ModelAdmin):
    list_display = ['passwd', 'hash_md5']
    search_fields = ['passwd']
admin.site.register(Md5s,Md5Admin)
