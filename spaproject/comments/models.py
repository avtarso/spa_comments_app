from django.core.validators import RegexValidator, URLValidator
from django.db import models

class Comment(models.Model):

    user_name = models.CharField(
        max_length=40,
        validators=[RegexValidator(r'^[a-zA-Z0-9]+$', 'Имя пользователя может содержать только латинские буквы и цифры!')]
    )
    e_mail = models.EmailField(
        max_length=255,
        error_messages={'invalid': 'Некорректный адрес электронной почты!'}
    )
    home_page = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[URLValidator(message='Некорректный URL!')]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] ## проверить как выглядит из админки
