# Create your models here.

from django.db import models
from django.conf import settings
from django.utils import timezone


class Post (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Cv(models.Model):

    #field
    author_name = models.CharField(max_length=20, help_text='name of author')
    address = models.TextField()
    phone_no = models.IntegerField()
    linkedIn = models.URLField()
    profile = models.TextField()
    skills = models.TextField()
    projects = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    extra_curricular = models.TextField()

    def __str__(self):
        return self.author_name

    def publish(self):
        self.save()    
