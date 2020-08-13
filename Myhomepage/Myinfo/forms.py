from django.forms import ModelForm
from .models import Myinfo

class MyinfoForm(ModelForm):
    class Meta:
        model = Myinfo
        fields = ['name','photo','email','github_link','skill','sns','introduction']
