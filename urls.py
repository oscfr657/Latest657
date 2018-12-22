
from django.conf.urls import url
from latest657 import views

urlpatterns = [
    url('^api/latestpost/', views.latest_post, name='latestpost'),
]
