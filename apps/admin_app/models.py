from django.db import models
import bcrypt
import re
import os
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if 'email' in postData:
            if len(User.objects.filter(email=postData['email'])) < 1:
                errors['login'] = "Login failed"
            elif 'pw' in postData:
                this_user = User.objects.filter(email=postData['email'])
                if not bcrypt.checkpw(postData['pw'].encode(), this_user[0].password.encode()):
                    errors['login'] = "Login failed"

        if 'newEmail' in postData:
            if not EMAIL_REGEX.match(postData['newEmail']):
                errors['email'] = "Please enter a valid email"

        if 'old_pw' and 'new_pw' and 'confirm_new_pw' in postData:
            if (len(postData['new_pw']) > 0 or len(postData['confirm_new_pw']) > 0) and len(postData['old_pw']) < 1:
                errors['old_pw'] = "Please enter your old password"
            if len(postData['old_pw']) > 0:
                this_user = User.objects.filter(id=postData['user_id'])
                if not bcrypt.checkpw(postData['old_pw'].encode(), this_user[0].password.encode()):
                    errors['old_pw'] = "Password incorrect"
                elif bcrypt.checkpw(postData['old_pw'].encode(), this_user[0].password.encode()):
                    if len(postData['new_pw']) < 8:
                        errors['new_pw'] = "New password must be at least 8 characters"
                    if (postData['confirm_new_pw']) != (postData['new_pw']):
                        errors['confirm_new_pw'] = "Passwords must match"
        return errors

class GalleryManager(models.Manager):
    def basic_validator(self, postFiles):
        errors={}
        if 'image' not in postFiles:
            errors['image'] = "Please choose an image to upload"
        return errors

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Gallery(models.Model):
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GalleryManager()

    def delete(self, *args, **kwargs):
        print(settings.MEDIA_ROOT)
        self.image.delete()
        super().delete(*args, **kwargs)

