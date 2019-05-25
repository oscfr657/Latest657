# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from io import BytesIO

from time import time

import magic
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.db import models


DIRECTORY = 'latest657'

IMAGE_TYPES = ['image/png',
               'image/jpeg',
               'image/jpg',
               'image/gif',
               'image/svg']

AUDIO_TYPES = ['audio/ogg',
               'audio/mpeg',
               'audio/wav']

VIDEO_TYPES = ['video/mp4',
               'video/webm',
               'video/ogg']


def unique_file_name(instance, filename):
    timestamp_time = int(time())
    path = u'{}/{}-{}'.format(DIRECTORY, timestamp_time, filename)
    return path


def validate_image(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if file_type not in IMAGE_TYPES:
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


def validate_audio(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if file_type not in AUDIO_TYPES:
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


def validate_video(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if file_type not in VIDEO_TYPES:
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


class Post(models.Model):
    # site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    image_file = models.ImageField(
        upload_to=unique_file_name,
        validators=[validate_image],
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
    cover_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='#0000')

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

    def save(self, *args, **kwargs):
        # First doing a normal save
        super(Post, self).save(*args, **kwargs)
        # Then we try to optimize
        try:
            file_type = magic.from_buffer(
                self.image_file.file.read(),
                mime=True)
            image_file = self.image_file
            image = Image.open(image_file)
            ftype = image.format
            if image.mode not in ('L', 'RGBA'):
                image = image.convert('RGBA')
            picture_name, picture_extension = os.path.splitext(
                self.image_file.name)
            picture_extension = picture_extension.lower()
            filename = picture_name + '_picture' + picture_extension
            image_copy = image.copy()
            image_copy.thumbnail((600, 600))
            image_file = BytesIO()
            image_copy.save(image_file, ftype, quality=90)
            image_file.seek(0)
            suf = SimpleUploadedFile(filename,
                                     image_file.read(),
                                     content_type=file_type)
            self.image_file.save(suf.name, suf, save=False)
            super(Post, self).save()
        except (IOError, ValueError, AttributeError):
            pass  # We should probably log this.
