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
  rating = models.ForeignKey('Rating',on_delete=models.CASCADE, default='')

  class Meta:
    ordering = ['title']

  def __str__(self):
    return self.title

  def save_project(self):
    self.save()


class Rating(models.Model):
  design = models.IntegerField(default=0)
  usability = models.IntegerField(default=0)
  content = models.IntegerField(default=0)


class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField(max_length=500, blank=True)
  location = models.CharField(max_length=50, blank=True)
  occupation = models.CharField(max_length=70, blank=True)
  date_updated = models.DateField(null=True, blank=True)

  def __str__(self):
    return self.user.username

  def save_profile(self):
    self.save()


