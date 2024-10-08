from django.shortcuts import render
from django.views import View

from apps.settings.models import SiteTemplate


class IndexView(View):
    def get(self, request):
        current = SiteTemplate.objects.filter(is_active=True).first()
        return render(request, f'{current.current_theme}/index.html', {})
