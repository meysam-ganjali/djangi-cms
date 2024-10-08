from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from apps.accounts.forms import LoginForm
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
                messages.error(request,'کاربر یافت نشد.')
                return render(request,f'{self.current.current_theme}/login.html',{'login_form': login_form})
        else:
            return render(request, f'{self.current.current_theme}/login.html', {'login_form': login_form})