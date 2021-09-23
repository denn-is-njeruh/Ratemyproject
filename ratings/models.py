from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=70)
  image = CloudinaryField('image', default='photo.jpeg')
  description = models.TextField(default='project description here')
  link = models.URLField(max_length=300, default='')

  class Meta:
    ordering = ['title']

  def __str__(self):
      return self.title