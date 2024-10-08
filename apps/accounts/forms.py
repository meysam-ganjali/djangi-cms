from django import forms
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={
        'placeholder': 'شماره موبایل خود را وارد کنید',
        'class': 'form-control',
        'maxlength': '11',
    }))
    password = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور خود را وارد کنید',
        'class': 'form-control',
    }))

    def clean_user_phone(self):
        user_phone = self.cleaned_data.get('user_phone')

        if not user_phone.isdigit():
            raise ValidationError('شماره موبایل باید فقط شامل اعداد باشد.')

        if len(user_phone) != 11:
            raise ValidationError('شماره موبایل باید ۱۱ رقم داشته باشد.')

        if not user_phone.startswith('0'):
            raise ValidationError('شماره موبایل باید با 0 شروع شود.')

        return user_phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError("کلمه عبور باید از 6 کاراکتر کمتر نباشد")
        return password
