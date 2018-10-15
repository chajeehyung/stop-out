from django.db import models

__all__ = (
    'University',
    'Students',
)

class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.ManyToOneRel(University)

    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

