from django import forms
from .models import  KhachHang
from django.contrib.auth.forms  import UserCreationForm



class DKForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = ["username","password","hoTen","SDT","diaChi","email"]