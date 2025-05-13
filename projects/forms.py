from django import forms
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'github_link', 'tags', 'contributors']
        widgets = {
            'contributors': forms.SelectMultiple(attrs={'class': 'form-select select2'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
        if user:
            self.fields['contributors'].queryset = User.objects.exclude(id=user.id)

