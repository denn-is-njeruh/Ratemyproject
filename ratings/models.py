from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=70)
  image = CloudinaryField('image', default='photo.jpeg')
  description = models.TextField(default='project description here')
  link = models.URLField(max_length=300, default='')
  username = models.ForeignKey(User,on_delete=models.CASCADE, default='1')

  class Meta:
    ordering = ['title']

  def __str__(self):
    return self.title


class Rating(models.Model):
  design = models.IntegerField(default=0)
  usability = models.IntegerField(default=0)
  content = models.IntegerField(default=0)
