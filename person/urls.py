from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', Register.as_view(), name='reg'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('home', profile, name='home'),
    path("login/", CustomLogin.as_view(), name='login'),
    path('registration', Registration.as_view(), name= 'registration')
]