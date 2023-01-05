from django.db import models
from django.contrib.auth.models import User


# Create your models here.  

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
  name =  models.CharField(max_length=200, null=True)
  profilepic = models.ImageField(null=True, blank=True) 
  email =  models.EmailField(max_length=300, editable=False)
  bio = models.CharField(max_length=500)
  location = models.CharField(max_length=100, default="")
  token = models.IntegerField(default=1, editable=False)
 
 
  def __str__(self):
        return str(self.name)

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
  quantity = models.IntegerField(default=1, editable=False)
  amount = models.IntegerField(default=0)
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
  user = models.OneToOneField(Profile, on_delete=models.SET_NULL,null=True, blank=True)
  date_swapped = models.DateTimeField(auto_now_add=True)


  @property
  def get_cart_total(self):
    swapitems = self.swapitem_set.all()
    total = sum([item.get_total for item in swapitems])
    return total

  print("hello",get_cart_total)


  @property
  def get_cart_items(self):
    swapitems = self.swapitem_set.all()
    total = sum([item.quantity for item in swapitems])
    return total

  @property
  def shipping(self):
    shipping = False
    swapitems = self.swapitem_set.all()
    for i in swapitems:
      if i.book.amount > 0:
        shipping = True
    return shipping
    
  def __str__(self):
        return str(self.id)  
class SwapItem (models.Model):
  swap = models.ForeignKey(Swap, on_delete=models.SET_NULL,null=True, blank=True)
  recipient = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
  book = models. ForeignKey(Book, on_delete=models.SET_NULL,null=True, blank=True)
  quantity = models.IntegerField(default=1, null = True, blank=True,editable=False)
  complete = models.BooleanField(default=False)
 
 
  @property
  def get_total(self):
    total = self.book.amount 
    return total


  


   

class Wishlist (models.Model):
  user = models.OneToOneField(Profile, on_delete=models.SET_NULL,null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return str(self.id)

class WishlistItem (models.Model):
  wishlist = models.ForeignKey(Wishlist, on_delete=models.SET_NULL,null=True, blank=True)
  book = models.ForeignKey(Book, on_delete=models.SET_NULL,null=True, blank=True)
  quantity = models.IntegerField(default=1, null = True, blank=True)


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