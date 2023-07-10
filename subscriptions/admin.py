from django.contrib import admin
from .models import Plan, PayPal, Subscription

# Register your models here.

admin.site.register(Plan) 
admin.site.register(PayPal) 
admin.site.register(Subscription) 