from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    img=models.ImageField(upload_to='static/api/images/')