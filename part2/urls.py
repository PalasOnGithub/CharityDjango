from django.urls import path
from .views import*

urlpatterns = [
    path('<uuid:nek>/' , DetailBlog , name='detailpage'),
    path('' , IndexPage , name = "indexpage"),
    path('get-access-error' , AccessPage),

]