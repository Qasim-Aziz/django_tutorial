from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError


def min_length_check(val):
    if len(val) <= 10:
        raise ValidationError("%(val)s Must be greater than 10", params={"val":
    val})

class Posts(models.Model):
    

    title = models.CharField(validators=[min_length_check], max_length=255)
    content = models.TextField(validators=[min_length_check])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager
    def __str__(self):
        return self.title

class Category(models.Model):
    

    title = models.CharField(validators=[min_length_check],max_length=255)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager
    def __str__(self):
        return self.title


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
  
