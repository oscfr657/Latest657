# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import Http404

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from latest657.models import Post
from latest657.serializers import PostSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def latest_post(request):
    try:
        post = Post.objects.filter(pub_date__isnull=False).latest('pub_date')
    except Post.DoesNotExist:
        raise Http404
    serializer = PostSerializer(post)
    return Response(serializer.data)
