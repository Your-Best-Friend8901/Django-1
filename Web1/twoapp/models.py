from django.db import models

# Create your models here.
class User(models.Model):
    nick = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.nick} | {self.password}'

 
