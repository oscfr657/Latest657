
from rest_framework import serializers

from latest657.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'pk', 'pub_date', 'text',
            'image_file', 'audio_file', 'video_file')
