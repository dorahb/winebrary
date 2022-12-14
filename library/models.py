from django.db import models
from django.contrib.auth.models import User

# Create your models here.  

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
  name =  models.CharField(max_length=200, null=True)
  profilepic = models.ImageField(null=True, blank=True) 
  email =  models.EmailField(max_length=300)
  bio = models.CharField(max_length=500)
  location = models.CharField(max_length=100, default="")
 
  def __str__(self):
        return self.name 

  @property
  def profilepicURL(self):
    try:
      url = self.profilepic.url
    except:
      url = ''
    return url
     

class Book(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  image = models.ImageField(blank=False) 
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=1000)
  pub_date = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=1)
  location = models.CharField(max_length=100, default="")

  def __str__(self):
      return self.title   

  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url
  

class Swap (models.Model):
  recipient = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
  book = models. ForeignKey(Book, on_delete=models.SET_NULL,null=True, blank=True)
  date_swapped = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False)
 
 
  def __str__(self):
        return str(self.recipient)

class Wishlist (models.Model):
  user = models.OneToOneField(Profile, on_delete=models.SET_NULL,null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return str(self.id)

class WishlistItem (models.Model):
  wishlist = models.ForeignKey(Wishlist, on_delete=models.SET_NULL,null=True, blank=True)
  book = models.ForeignKey(Book, on_delete=models.SET_NULL,null=True, blank=True)
  quantity = models.IntegerField(default=0, null = True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)


  def __str__(self):
        return str(self.wishlist)



class ShippingAddress (models.Model):
  user = models. ForeignKey(Profile, on_delete=models.SET_NULL,null=True, blank=True)
  swap = models. ForeignKey(Swap, on_delete=models.SET_NULL,null=True, blank=True)
  address = models.CharField(max_length=200,null=False)
  town = models.CharField(max_length=200,null=False)
  region = models.CharField(max_length=200,null=False)
  country = models.CharField(max_length=200,default='SOME STRING')
  date = models.DateTimeField(auto_now_add=True)
 

  def __str__(self):
        return str(self.address)