from django import forms 
from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile 

class UpdateProfileForm(ModelForm):
    class Meta: 
        model = Profile 
        fields = ('favourite_systems', 'u_type', 'age')
    
class UpdateUserForm(ModelForm):
    """Form definition for UpdateUser."""

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم'}), label='اسم المستخدم')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'الاسم الأول'}), label="الاسم الأول")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'الاسم الأخير'}), label="الاسم الأخير")

    class Meta:
        """Meta definition for UpdateUserform."""

        model = User 
        fields = ('username', 'first_name', 'last_name')
