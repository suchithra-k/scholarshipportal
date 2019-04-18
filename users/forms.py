from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .user_constants import UserConstant


class StudentSignUpForm(UserCreationForm):

    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=255)
    gender = forms.ChoiceField(choices=UserConstant.GENDER_CHOICES)
    user_role = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender',
                  'birth_date', 'email', 'password1', 'password2', )
