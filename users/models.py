from django.db import models
from system.models import * 
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.db.models.signals import post_save 

# Create your models here.

TYPE_CHOICES = (
    ('male', 'ذكر'), 
    ('female', 'أنثى')
)

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    favourite_systems = models.ManyToManyField(System, related_name='profiles', verbose_name="التقنيات المفضلة", blank=True )
    age = models.IntegerField(default=16, verbose_name="العمر") 
    u_type = models.CharField(choices=TYPE_CHOICES, verbose_name="النوع", max_length=20, null=True, blank=True) 
    

    def __str__(self):
        return f"{self.user} | Profile"
    
    class Meta:
        verbose_name='الملف الشخصي'
        verbose_name_plural ="الملفات الشخصية"