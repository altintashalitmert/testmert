from pydoc import describe
from django.db import models


class test(models.Model):
    title = models.CharField(max_length=360, blank=False, null=True)
    description = models.CharField(max_length=360, blank=False, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

class rehber(models.Model):
    isim = models.CharField(max_length=360, blank=False, null=True)
    soyisim = models.CharField(max_length=360, blank=False, null=True)
    numara = models.CharField(max_length=360, blank=False, null=True)
    email = models.CharField(max_length=360, blank=False, null=True)
    gsm = models.CharField(max_length=360, blank=False, null=True)
