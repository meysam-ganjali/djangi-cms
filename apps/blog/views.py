from django.shortcuts import render

from apps.settings.models import SiteTemplate


def index(request):
    current = SiteTemplate.objects.filter(is_active=True).first()
    return render(request,f'{current.current_theme}/index.html',{'current':current.current_theme})