from django import forms
from .models import Pblog

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Pblog
        fields = ['p_title','p_body','p_link']