
from django.conf.urls import url

from latest657 import views
from latest657.feed import PostFeed

urlpatterns = [
    url('^api/latestpost/', views.latest_post, name='latestpost'),
    url(r'^feed/$', PostFeed(), name='rss-feed'),
]
