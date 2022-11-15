from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.  

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  profilepic = CloudinaryField('image')
  email =  models.CharField(max_length=100)
  bio = models.CharField(max_length=500)
 
  def __str__(self):
        return self.user 

class Book(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  image = CloudinaryField('image')  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=1000)
  pub_date = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=100, default="")

  def __str__(self):
      return self.title   
  
