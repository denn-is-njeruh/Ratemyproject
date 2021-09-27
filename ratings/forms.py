from django.db.models import fields
from ratings.models import Profile,Project
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Your forms here
class NewUserForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


  def save(self,commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('user','location','occupation')


class UploadProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ('title','image','description','link','rating')