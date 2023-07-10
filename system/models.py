from django.db import models
from django.utils.text import slugify

# Create your models here.
class System(models.Model):

    name = models.CharField(verbose_name="الاسم", max_length=100)
    img = models.ImageField(upload_to='systems/logos/', verbose_name="صورة لوجو النظام")

    overview = models.TextField(null=True, blank=True, verbose_name="ملخص سريع") 

    slug = models.SlugField(max_length=200, verbose_name="اسم الرابط", null=True, blank=True, allow_unicode=True)  

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.name)  
        super(System, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = ("نظام قاعدة بيانات")
        verbose_name_plural = ("أنظمة قواعد بيانات")


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="النوع") 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'نوع'
        verbose_name_plural = 'أنواع الحقول'

class Field(models.Model):

    system = models.ForeignKey(System, verbose_name="قاعدة البيانات", on_delete=models.CASCADE)

    # f_type = models.ForeignKey(Type, verbose_name=("نوع الحقل"), on_delete=models.SET_DEFAULT, default='غير معروف') 

    f_type = models.CharField(max_length=75, verbose_name="نوع الحقل")

    syntax = models.TextField(verbose_name="الجملة الأساسية (Syntax)")

    class Meta:
        verbose_name = ("حقل")
        verbose_name_plural = ("الحقول")

    def __str__(self):
        return f'{self.system} | {self.f_type}'

