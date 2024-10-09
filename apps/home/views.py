from django.shortcuts import render
from django.views import View

from apps.banner.models import Banner
from apps.settings.models import SiteTemplate


class IndexView(View):
    current = SiteTemplate.objects.filter(is_active=True).first()

    def get(self, request):
        data = {}
        banner = Banner.objects.filter(is_active=True)
        data['banners'] = banner
        return render(request, f'{self.current.current_theme}/index.html', {'data':data})
