from django.contrib import admin
from django.urls import path, include
from comments.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('comments.urls')),
    path('', index, name='index'),
]