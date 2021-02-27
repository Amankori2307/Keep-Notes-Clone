from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False) # changes email to unique and blank to false
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 


class Label(models.Model):
    userRef = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



class Notes(models.Model):
    userRef = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(blank = True, default="", max_length=255)
    text = models.TextField(blank = True, default="")
    labelRef = models.ForeignKey(Label, on_delete=models.CASCADE, null=True)
    isDeleted = models.BooleanField(default=False) # If true this note will be shown in deleted items
    isArchived = models.BooleanField(default=False) # If true then this note will be shown in archived items
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class MediaChoices(models.TextChoices):
    # KILOGRAM = 'kg', _('Kilogram')
    IMAGE = 'img', _('IMAGE')
    AUDIO = 'audio', _('AUDIO')

class Media(models.Model):
    noteRef = models.ForeignKey(Notes, on_delete=models.CASCADE)
    mediaType = models.CharField(choices=MediaChoices.choices, max_length=5)
    value = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class CheckBox(models.Model):
    noteRef = models.ForeignKey(Notes, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    text = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Collaberator(models.Model):
    collaberatorRef = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    noteRef = models.ForeignKey(Notes, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
