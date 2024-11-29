from django.db import models

class Comment(models.Model):

    user_name = models.CharField(max_length=255) 
    e_mail = models.EmailField(max_length=255)
    home_page = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] ## проверить как выглядит из админки
