from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'github', 'linkedin', 'profile_picture', 'website', 'location')


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'github', 'linkedin', 'profile_picture', 'website', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password fields if they exist
        if 'password' in self.fields:
            del self.fields['password']
        if 'password2' in self.fields:
            del self.fields['password2']
