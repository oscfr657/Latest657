
from rest_framework import serializers

from latest657.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'pk', 'pub_date', 'title', 'text',
            'image_file', 'audio_file', 'video_file', 'cover_color', 'cover_opacity')
