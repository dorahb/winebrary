from django.urls import path
from . import views
from .views import search

urlpatterns = [
  path('',views.index, name ='index'),
  path('profile/',views.profile, name='profile'),
  path('search/',search.as_view(), name='search'),
  path('submit/',views.submit, name='submit'),
  path('update_item/',views.updateItem, name='update_item'),
  path('update_swap/',views.updateSwap, name='update_swap'),
  path('login/',views.loginPage, name='login'),
  path('logout/',views.logoutUser, name='logout'),
  path('signup/',views.signup, name='signup'),
  path('updateprofile/',views.updateprofile, name='updateprofile'),
  path('swap/',views.swap, name='swap'),

]
