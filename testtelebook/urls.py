from django.urls import path
from .views import *

urlpatterns = [
    path('', TeleView.as_view(), name='home'),
    path('search/', TeleSearch.as_view(), name='search'),
    path('add_contact/', add_contact, name='add_contact'),
    path('delete_contact/<int:pk>', delete_contact, name='delete_contact'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
