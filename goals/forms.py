from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'due_date', 'is_completed']
        widgets = {
            'is_completed': forms.CheckboxInput(),
        }