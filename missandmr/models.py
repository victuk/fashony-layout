from django.db import models

# Create your models here.

class youtubelink(models.Model):
    title = models.CharField(max_length=50, default='')
    link = models.TextField(max_length=455, default='')
    def __str__(self):
        return self.title

class contestant(models.Model):
    name = models.CharField(max_length=50, default='')
    picture = models.ImageField(upload_to='images/', default='')
    contestantsCode = models.CharField(max_length=455, default='')
    email = models.CharField(max_length=455, default='')
    gender = models.CharField(choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ], max_length = 10, default="Male")
    description = models.TextField(max_length=455, default='')
    amount = models.CharField(max_length=455, default='N5,000')
    status = models.TextField(
        choices = [
        ('Not Paid', 'Not Paid'),
        ('Paid', 'Paid')
    ],max_length=20, default='Paid')
    def __str__(self):
        return self.name

class contact(models.Model):
    fullName = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=455, default='')
    message = models.TextField(max_length=455, default='')
    def __str__(self):
        return self.fullName