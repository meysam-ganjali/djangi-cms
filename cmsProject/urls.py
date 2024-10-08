from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', include('apps.home.urls', namespace='home')),
                  path('ckeditor', include('ckeditor_uploader.urls')),
                  path('accounts/', include('apps.accounts.urls', namespace='accounts')),
                  path('', include('apps.blog.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'پنل مدیریت'
