from django import forms

from .models import User


class UserForms(forms.ModelForm):
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput(), label='رمز عبور')

    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'first_name', 'last_name', 'age', 'gender_type', 'password']
