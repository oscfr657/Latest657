# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.utils import timezone

from latest657.models import Post

class PostFeed(Feed):
    """ Class Docstring ?
    """
    title = "Latest 657 Feed"
    link = ""
    description = "All the latest things 657."

    @classmethod
    def items(cls):
        posts = Post.objects.filter(pub_date__isnull=False).filter(
            pub_date__lte=timezone.now()
            ).order_by('pub_date')
        return posts

    @classmethod
    def item_title(cls, item):
        return item.title

    def item_description(self, item):
        return item.text

    @classmethod
    def item_pubdate(cls, item):
        return item.pub_date
