from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class prospects(models.Model):
    name=models.CharField(max_length=100, unique=False)
    email=models.CharField(max_length=100, unique=False)
    type=models.CharField(max_length=100, unique=False)
    feel=models.CharField(max_length=100, unique=False)
    description=models.TextField(max_length=500, blank=False)
    budget=models.CharField(max_length=100, unique=False)
    date=models.DateTimeField(default=datetime.now, blank=False)

    def __unicode__(self):
        return self.name

class feedback(models.Model):
    name=models.CharField(max_length=100, unique=False)
    email=models.CharField(max_length=100, unique=False)
    enquiry=models.CharField(max_length=100, unique=False)
    question=models.CharField(max_length=100, unique=False)
    number=models.CharField(max_length=100, unique=False)
    date=models.DateTimeField(default=datetime.now, blank=False)

    def __unicode__(self):
        return self.name

class portfolio(models.Model):
    project_title=models.CharField(max_length=100, unique=False)
    project_link=models.CharField(max_length=100, unique=False)
    project_image1=models.ImageField(upload_to='images', verbose_name='image', blank=False)
    project_image2=models.ImageField(upload_to='images', verbose_name='image2', blank=True)
    project_image3=models.ImageField(upload_to='images', verbose_name='image3', blank=True)
    date=models.DateTimeField(default=datetime.now, blank=False)
    def __unicode__(self):
        return self.project_link
