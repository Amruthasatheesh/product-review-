from django.db import models




class productrev(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phoneno=models.IntegerField()
    password=models.CharField(max_length=25)





