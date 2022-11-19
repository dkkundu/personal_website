# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(
        upload_to='cv/%Y/%m/%d/', null=True, blank=True
    )
    url = models.URLField(
        max_length=255, null=True, blank=True
    )
    is_active = models.BooleanField(default=False)  # space-separated values

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            for cv in CV.objects.filter(is_active=True):
                cv.is_active = False
                cv.save()

        super(CV, self).save(*args, **kwargs)
