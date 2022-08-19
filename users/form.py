from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    # password2=forms.CharField()

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            # 'password2'
        ) 
        # labels={'password2':'password again'}


