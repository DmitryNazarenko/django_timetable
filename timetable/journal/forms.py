from django import forms

from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['record']
        widgets = {
           'record':forms.Textarea(attrs={'class':'custom_textarea'}),
        }
