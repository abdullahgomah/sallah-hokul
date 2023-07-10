from django.db import models
import datetime
from django.contrib.auth.models import User 

# Create your models here.
class Plan(models.Model):

    name = models.CharField(max_length=100, verbose_name="اسم الباقة", unique=True)  

    price = models.IntegerField(verbose_name="سعر الباقة (دولار)")

    description = models.TextField(max_length=200, verbose_name="وصف بسيط للباقة")

    validty = models.IntegerField(default=0, verbose_name="مدة الباقة")  

    ## هنا سنضيف صلاحيات الباقة

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'باقة'
        verbose_name_plural = 'باقات'

class Subscription(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE) 

    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True) 

    start_date = models.DateField(null=True, blank=True)  

    end_date = models.DateField(null=True, blank=True) 

    class Meta:
        verbose_name = 'اشتراك' 
        verbose_name_plural = 'اشتراكات'

    def save(self, *args, **kwargs):

        plan_validty = datetime.timedelta(days=self.plan.validty) 

        self.end_date = self.start_date + plan_validty

        super(Subscription, self).save(*args, **kwargs)


class PayPal(models.Model):
    client_id = models.CharField(max_length=255) 
    secret = models.TextField() 
    access_token = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=10)
     
    class Meta:
        verbose_name = 'حساب باي بال'
        verbose_name_plural = 'حسابات باي بال'