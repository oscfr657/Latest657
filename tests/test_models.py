
from django.test import TestCase
from ..models import Post


class PostTest(TestCase):
    """ Test module for Post model """

    def setUp(self):
        Post.objects.create(text='PostOne')
        Post.objects.create(text='PostTwo')

    def test_collection_title(self):
        post_one = Post.objects.get(text='PostOne')
        post_two = Post.objects.get(text='PostTwo')
        self.assertEqual(post_one.text, 'PostOne')
        self.assertEqual(post_two.text, 'PostTwo')
