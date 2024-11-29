from django.contrib import admin
from django.urls import path, include
from comments.views import index
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('comments.urls')),
    path('', index, name='index'),

    path('captcha/', include('captcha.urls')),  # Для предоставления изображения капчи
    path('api/check-captcha/', views.check_captcha, name='check_captcha'),  # Для проверки ответа

    path('api/get-captcha/', views.get_captcha, name='get_captcha'),
    
    

]