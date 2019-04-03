
from rest_framework import status
from django.test import TestCase, Client
from ..models import Post
from ..serializers import PostSerializer

client = Client()


class GetLatestPostTest(TestCase):
    """ Test module for GET latest Post API """

    def setUp(self):
        Post.objects.create(text='PostOne')

    def test_get_latest_post_fail(self):
        response = client.get('/latest/api/latestpost/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_latest_post(self):
        Post.objects.create(text='PostTwo', pub_date='2018-10-10 00:00')
        Post.objects.create(text='PostThree', pub_date='2018-10-11 00:00')
        response = client.get('/latest/api/latestpost/')
        post = Post.objects.get(text='PostThree')
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_latest_post_pub_date_not_null(self):
        Post.objects.create(text='PostTwo', pub_date='2018-10-10 00:00')
        Post.objects.create(text='PostThree')
        response = client.get('/latest/api/latestpost/')
        post = Post.objects.get(text='PostTwo')
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
