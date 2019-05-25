# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from latest657.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('pub_date', 'title', 'text', 'image_file',
              'audio_file', 'video_file', 'cover_color')
    date_hierarchy = 'pub_date'


admin.site.register(Post, PostAdmin)
