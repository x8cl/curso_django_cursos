from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        #creo un diccionario con los errores key/value
        errors = {}
        #valido que el campo "title" tenga al menos 5 caracteres y saco los espacios con strip
        if len(postData["name"].strip()) < 5:
            errors["name"] = "Name must be at least 5 characters"
        #valido que el campo "description" tenga al menos 2 caracteres y saco los espacios con strip
        if len(postData["desc"].strip()) < 15:
            errors["desc"] = "Description must be at least 15 characters"
        #retorno errores
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    class Meta:
        app_label = "core"
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
