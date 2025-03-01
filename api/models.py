from django.db import models
from django.db.models import SET_NULL, ManyToManyField
from django_extensions.db.models import TimeStampedModel
from taggit.managers import TaggableManager


class Category(TimeStampedModel):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class Post(TimeStampedModel):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(unique=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title