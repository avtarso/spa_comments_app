import bleach
from rest_framework import serializers
from .models import Comment


ALLOWED_TAGS = ['a', 'code', 'i', 'strong', 'p']
ALLOWED_TAGS_ATTRIBUTES = {'a': ['href', 'title']}


def sanitize_html(input_html):
    return bleach.clean(input_html, tags=ALLOWED_TAGS, attributes=ALLOWED_TAGS_ATTRIBUTES, strip=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['text'] = sanitize_html(representation['text'])
        return representation
    
    def html_representation(self):
        representation = self.to_representation(self.instance)
        excluded_fields = ['e_mail']  # Поля, которые нужно исключить
        return {key: value for key, value in representation.items() if key not in excluded_fields}