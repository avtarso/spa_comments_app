from django.contrib import admin

from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'e_mail', 'created_at', 'text')
    search_fields = ('user_name', 'text')
