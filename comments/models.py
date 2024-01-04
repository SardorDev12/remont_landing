from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    comment = models.TextField()
