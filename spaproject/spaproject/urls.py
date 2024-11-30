from django.contrib import admin
from django.urls import path, include
from comments.views import index
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('comments.urls')),
    path('', index, name='index'),
    path('api/get-captcha/', views.get_captcha, name='get_captcha'),
    path('api/verify-captcha/', views.verify_captcha, name='verify_captcha'),
]

# Временная обработка статики
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
