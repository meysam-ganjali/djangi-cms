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

    def clean_phone(self):
        user_phone = self.cleaned_data.get('phone')
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


class RegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={
        'placeholder': 'شماره موبایل خود را وارد کنید',
        'class': 'form-control',
        'maxlength': '11',
    }))
    password = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور خود را وارد کنید',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': 'تکرار رمز عبور خود را وارد کنید',
        'class': 'form-control',
    }))
    name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
        'placeholder': 'نام خود را وارد کنید',
        'class': 'form-control',
        'maxlength': '1000',
    }))
    family = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': ' نام خانوادگی خود را وارد کنید',
        'class': 'form-control',
        'maxlength': '50',
    }))

    def clean_phone(self):
        user_phone = self.cleaned_data.get('phone')
        if User.objects.filter(user_phone=user_phone).exists():
            raise ValidationError('کاربر با این شماره تلفن موجود است')
        if len(user_phone) != 11:
            raise ValidationError('شماره موبایل باید ۱۱ رقم داشته باشد.')

        if not user_phone.startswith('0'):
            raise ValidationError('شماره موبایل باید با 0 شروع شود.')
        return user_phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if len(password) < 6:
            raise ValidationError('کلمه عبور کمتر از 6 کاراکتر است')
        if len(confirm_password) < 6:
            raise ValidationError('تکرار کلمه عبور کمتر از 6 کاراکتر است')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('رمز عبور و تکرار آن مطابقت ندارند.')

        return cleaned_data