from django import forms 

from .models import myModel
class TodoModelForm(forms.ModelForm):
    
    class Meta:
        model = myModel
        fields = ['text']
