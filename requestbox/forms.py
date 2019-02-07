from django import forms
from .models import Req

class ReqCreateForm(forms.ModelForm):

    class Meta:
        model = Req
        fields = '__all__'
