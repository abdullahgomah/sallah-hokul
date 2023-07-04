from django.db import models

# Create your models here.
class Plan(models.Model):

    name = models.CharField(max_length=100, verbose_name="اسم الباقة", unique=True)  

    price = models.IntegerField(verbose_name="سعر الباقة (دولار)")

    description = models.TextField(max_length=200, verbose_name="وصف بسيط للباقة")

    ## هنا سنضيف صلاحيات الباقة

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'باقة'
        verbose_name_plural = 'باقات'

class Subscription(models.Model):


    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True) 



    class Meta:
        verbose_name = 'اشتراك' 
        verbose_name_plural = 'اشتراكات'


class PayPal(models.Model):
    client_id = models.CharField(max_length=255) 
    secret = models.TextField() 
    access_token = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=10)
     
    class Meta:
        verbose_name = 'حساب باي بال'
        verbose_name_plural = 'حسابات باي بال'