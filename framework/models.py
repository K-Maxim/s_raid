from django.db import models


class FrameworkModel(models.Model):
    name = models.CharField(max_length=25, verbose_name='название', blank=True)
    language = models.CharField(max_length=50, verbose_name='язык программирования', blank=True)

