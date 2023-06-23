from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Type, System, Field
# Register your models here.

admin.site.register(Type)
admin.site.register(System)
admin.site.register(Field)

admin.site.site_header = 'سلة الحقول'
admin.site.site_title = 'سلة الحقول'