from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 15)
    message = models.TextField()

    def __str__(self):
        return self.full_name
