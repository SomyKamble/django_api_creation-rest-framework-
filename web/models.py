from django.db import models

# Create your models here.

class sampleweb(models.Model):
    name= models.CharField(max_length=200)
    age = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name
