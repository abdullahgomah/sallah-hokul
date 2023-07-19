from django.db import models

# Create your models here.
class Info(models.Model):
    about = models.TextField() 

    def __str__(self) -> str:
        return self.about[:10]
    
    class Meta: 
        verbose_name_plural = 'معلومات'


class Home(models.Model):
    heading = models.CharField(max_length=255, verbose_name='الجملة الرئيسية') 
    sub_heading = models.CharField(max_length=255, verbose_name="الجملة الفرعية") 
    btn_text = models.CharField(max_length=100, verbose_name="نص الزر الرئيسي")
    btn_link = models.URLField(verbose_name="رابط الزر الرئيسي")

    def __str__(self):
        return str(self.heading)

    class Meta:
        verbose_name = 'الصفحة الرئيسية'
        verbose_name_plural = 'الصفحة الرئيسية'