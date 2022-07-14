from django.urls import path
from .views import *

urlpatterns = [
    path('', FilterList.as_view(), name='home'),
    path('add_contact/', add_contact, name='add_contact'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('edit_contact/', edit_contact, name='edit_contact'),
]
