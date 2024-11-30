from django.contrib import admin
from django.urls import path, include
from comments.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('comments.urls')),
    path('', index, name='index'),
    path('api/get-captcha/', views.get_captcha, name='get_captcha'),
    path('api/verify-captcha/', views.verify_captcha, name='verify_captcha'),

]