from django.contrib import admin
from itxx.sedb.models import People  

class SedbAdmin(admin.ModelAdmin):
    list_display = ['name','nickname','email','idcard','address','company','counttype','count','passtype','password']
    list_filter = ['counttype','passtype']
    search_fields = ['name','nickname','email']
admin.site.register(People,SedbAdmin)
