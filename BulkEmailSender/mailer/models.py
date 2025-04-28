from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates every time the record is saved
    
    def __str__(self):
        return self.name

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=100)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates every time the record is saved

    def __str__(self):
        return self.subject
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name