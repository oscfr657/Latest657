# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import time

import magic
from PIL import Image

from django.core.exceptions import ValidationError
from django.db import models


DIRECTORY = 'latest657'

def unique_file_name(instance, filename):
    timestamp_time = int(time())
    path = u'{}/{}-{}'.format(DIRECTORY, timestamp_time, filename)
    return path


audio_types = ['audio/ogg',
               'audio/mpeg',
               'audio/wav']

video_types = ['video/mp4',
               'video/webm',
               'video/ogg']


def validate_audio(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if not (file_type in audio_types):
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


def validate_video(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        print('test')
        print(file_type)
        if not (file_type in video_types):
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


class Post(models.Model):
    pub_date = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=50, blank=True, null=True)
    image_file = models.ImageField(
        upload_to=unique_file_name,
        blank=True,
        null=True)
    audio_file = models.FileField(
        upload_to=unique_file_name,
        validators=[validate_audio],
        blank=True,
        null=True)
    video_file = models.FileField(
        upload_to=unique_file_name,
        validators=[validate_video],
        blank=True,
        null=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        if self.text:
            return u'%s' % self.text
        return u'%s' % self.pk

    def __str__(self):
        if self.text:
            return u'%s' % self.text
        return u'%s' % self.pk
