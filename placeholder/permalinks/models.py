from django.db import models

# Create your models here.


class PholderType(models.Model):
    internal_name = models.CharField(max_length=50, null=False)
    display_name = models.CharField(max_length=50, null=False)


class Pholder(models.Model):
    name = models.CharField(max_length=30, null=False)
    pholder_type = models.ForeignKey(PholderType, on_delete=models.CASCADE)


class ShortLink(models.Model):
    url_hash = models.CharField(max_length=20, null=False)
    pholder = models.ForeignKey(Pholder, on_delete=models.CASCADE)
