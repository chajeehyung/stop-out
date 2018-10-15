from django.db import models

class Students(models.Model):
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

