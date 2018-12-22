try:
    from django.urls import path
except  ImportError:
    from django.conf.urls import url as path

from rest_framework.urlpatterns import format_suffix_patterns
from latest657 import views

urlpatterns = [
    path('^api/latestpost/', views.latest_post, name='latestpost'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
