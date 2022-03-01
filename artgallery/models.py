import os
from django.db import models

# Create your models here.

FORSALE = {
    ('YES', 'YES'),
    ('NO', 'NO'),
}


def get_image_path(instance, filename):
    return os.path.join('', str(instance.title,), filename)


class Painting(models.Model):
    title = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=50, blank=False)
    dimension = models.CharField(max_length=20)
    medium = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path, default='none', blank=False)
    technique = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    sale = models.CharField(choices=FORSALE, max_length=4, default='NO')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

