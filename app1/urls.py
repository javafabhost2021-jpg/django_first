from django.urls import path
from app1.views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('register/',register_view, name = 'register'),
    path('login/', login_view, name ='login'),
    path('logout/', logout_view, name='logout'),
    path('post_create/', post_create, name= 'post_create'),
    path('post/<int:id>/delete',post_delete, name= 'post_delete'),
]


