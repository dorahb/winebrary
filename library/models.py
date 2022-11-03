from django.db import models

# Create your models here.
class Book(models.Model):
  image = models.ImageField(null=True, blank=True)  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=1000)
  pub_date = models.DateTimeField('date posted')