from django.urls import path, include
from .views import*


urlpatterns = [
    path('' , IndexPage , name='indexpage'),
    path('home/' , IndexPage , name='indexpage'),
    path('contact-us/' , ContactPage , name = 'Contact_us'),
    #main functionallity
    path('dashboard-user/', DashBoardPage , name= 'dashboard_user'),
    path('inprog' , RegisteringInformation , name='checking_state') ,
    #authontications 
    path('login/' , LoginPage , name='LoginPage'),
    path('checkpeace/' , LogCheck),
    path('logout/' , LogOutPage),
    path('register/' , RegistrationPage),
]