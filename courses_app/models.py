from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name'] = "Name must be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Please be more descriptive of the course"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = CourseManager()