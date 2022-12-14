from django.urls import path
from . import views



urlpatterns = [
  path('',views.index, name ='index'),
  path('profile/',views.profile, name='profile'),
  path('search/',views.search, name='search'),
  path('submit/',views.submit, name='submit'),
  path('update_item/',views.updateItem, name='update_item'),
  path('login/',views.loginPage, name='login'),
  path('logout/',views.logoutUser, name='logout'),
  path('signup/',views.signup, name='signup'),
  path('updateprofile/',views.updateprofile, name='updateprofile'),

]
