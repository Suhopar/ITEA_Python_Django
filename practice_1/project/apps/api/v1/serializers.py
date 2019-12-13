from rest_framework import serializers
from apps.core.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    category = serializers.CharField(read_only=True)
    description = serializers.CharField()
    text = serializers.CharField()
    pub_date = serializers.DateTimeField(read_only=True)
