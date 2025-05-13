from django import forms
from .models import DevLog

class DevLogForm(forms.ModelForm):
    class Meta:
        model = DevLog
        fields = ['project', 'title', 'content']
