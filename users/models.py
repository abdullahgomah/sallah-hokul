from django.db import models
from system.models import * 
from django.contrib.auth.models import User 

# Create your models here.

TYPE_CHOICES = (
    ('male', 'ذكر'), 
    ('female', 'أنثى')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    favourite_systems = models.ManyToManyField(System, related_name='profiles', verbose_name="التقنيات المفضلة")
    age = models.IntegerField(default=16, verbose_name="العمر") 
    u_type = models.CharField(choices=TYPE_CHOICES, verbose_name="النوع", max_length=20) 
    

    def __str__(self):
        return f"{self.user} | Profile"
    
    class Meta:
        verbose_name='الملف الشخصي'
        verbose_name_plural ="الملفات الشخصية"