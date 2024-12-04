from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import JsonResponse


class CommentsListCreateView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            message = {
                'id': comment.id,
                'user_name': comment.user_name,
                'text': comment.text,
            }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'comments',
                {
                    'type': 'new_comment',
                    'message': message
                }
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.likes +=1 
        comment.save()
        return JsonResponse({'likes': comment.likes})

def dislike_comment(request, comment_id):
    if request.method == 'POST':
        commen = get_obgect_or_404(Comment, id=comment_id)
        comment.dislikes -= 1
        comment.save()
        return JsonResponse({'dislikes': comment.dislikes})



def index(request):
    return render(request, 'comments/index.html')
