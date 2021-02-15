from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.modelSerializer):
    class Meta:
        models = Todo
        fields = ('id', 'title', 'body')