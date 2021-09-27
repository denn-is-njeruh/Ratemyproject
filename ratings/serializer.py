from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project,Profile


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','image','description','link')


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('user','bio','profile picture')