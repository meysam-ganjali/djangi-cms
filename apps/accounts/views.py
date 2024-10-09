from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from apps.accounts.forms import LoginForm, RegisterForm
from apps.accounts.models import User
from apps.utilities import generate_code, send_sms
from apps.settings.models import SiteTemplate


class LoginView(View):
    current = SiteTemplate.objects.filter(is_active=True).first()

    def get(self, request):
        return render(request, f'{self.current.current_theme}/login.html', {'login_form': LoginForm()})

    def post(self, request):
        login_form = LoginForm(request.POST)
        remember = request.POST.get('remember', 'off')
        if login_form.is_valid():
            phone = login_form.cleaned_data['phone']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                if remember == 'on':
                    request.session.set_expiry(60 * 60 * 24 * 2)
                else:
                    request.session.set_expiry(0)
                return redirect('home:index')
            else:
                messages.error(request, 'کاربر یافت نشد.')
                return render(request, f'{self.current.current_theme}/login.html', {'login_form': login_form})
        else:
            for field, errors in login_form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return render(request, f'{self.current.current_theme}/login.html', {'login_form': login_form})


class RegisterView(View):
    current = SiteTemplate.objects.filter(is_active=True).first()

    def get(self, request):
        return render(request, f'{self.current.current_theme}/register.html', {'register_form': RegisterForm()})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        confirm = request.POST.get('confirm', 'off')
        if confirm != 'on':
            messages.error(request, 'تیک شرایط و قوانین را میپذیرم. را بزنید')
            return render(request, f'{self.current.current_theme}/register.html', {'register_form': register_form})
        if register_form.is_valid():
            phone = register_form.cleaned_data['phone']
            password = register_form.cleaned_data['password']
            name = register_form.cleaned_data['name']
            family = register_form.cleaned_data['family']
            activation_code = generate_code(5)
            User.objects.create_user(
                name=name,
                family=family,
                user_phone=phone,
                password=password,
                active_code=activation_code
            )
            send_sms()#TODO:Send SMS for active account
            request.session['activation_code'] = activation_code
            request.session['phone'] = phone
            request.session['type'] = 'active'
            return redirect('accounts:activation')
        else:
            for field, errors in register_form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return render(request, f'{self.current.current_theme}/register.html', {'register_form': register_form})


class ActiveAcoountView(View):
    current = SiteTemplate.objects.filter(is_active=True).first()
    def get(self, request):
        return render(request, f'{self.current.current_theme}/activation.html')

    def post(self, request):
        activation_code = request.session.get('activation_code')
        phone = request.session.get('phone')
        user_active_code = request.POST.get('active_code','')

        if activation_code != user_active_code:
            messages.error(request,'کد فعالسازی اشتباه است')
            return render(request, f'{self.current.current_theme}/activation.html')
        else:
            try:
                user = User.objects.get(user_phone=phone)
                user.is_active = True
                user.active_code = generate_code(5)
                user.save()
                return redirect('home:index')
            except User.DoesNotExist:
                messages.error(request,'کاربر وجود ندارد')
                return render(request, f'{self.current.current_theme}/activation.html')


def custom_logout_view(request):
    logout(request)
    return redirect('home:index')
