from django.db import models

# Create your models here.

class MeteoDatas(models.Model):
    region = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.region
