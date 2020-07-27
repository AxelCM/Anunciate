from django.contrib import admin

from anuncios.models import Bulletin

class BulletinAdmin(admin.ModelAdmin):
    list_display = ['title' , 'price']


admin.site.register(Bulletin , BulletinAdmin)
