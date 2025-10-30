from rest_framework import serializers
from .models import Goodthing

class GoodthingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodthing
        fields = ['id', 'content', 'likes_count', 'not_good_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'likes_count', 'not_good_count']