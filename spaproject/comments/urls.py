from django.urls import path
from .views import CommentsListCreateView, index, like_comment, dislike_comment

urlpatterns = [
    path('comments/', CommentsListCreateView.as_view(), name='comment-list-create'),
    path('', index, name='index'),
    path('comments/<int:comment_id>/like/', like_comment, name='like_comment'),
    path('comments/<int:comment_id>/dislike/', dislike_comment, name='dislike_comment')
    ]
