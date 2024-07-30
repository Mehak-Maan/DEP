from django.urls import path
from .views import create,home,delete,update,user_login
urlpatterns = [
    path('home/',home,name="home"),
    path('create/',create,name='create') ,
    path('delete/<int:e_id>',delete,name='delete'),
    path('update/<int:e_id>',update,name="update") ,
    path('login/',user_login,name="login")
]