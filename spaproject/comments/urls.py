from django.urls import path
from .views import CommentsListCreateView, index

urlpatterns = [
    path('comments/', CommentsListCreateView.as_view(), name='comment-list-create'),
    path('', index, name='index'),
    ]
