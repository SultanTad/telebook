from django.contrib import messages
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django.views.generic import UpdateView

from .models import *
from .forms import AddNameContact, AddTypeContact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .filters import TeleBookFilter


class FilterList(FilterView):
    model = TypesInPhone
    filterset_class = TeleBookFilter
    template_name = 'index.html'


def edit_contact(request):
    contact = ContactInPhone.objects.all()
    types = TypesInPhone.objects.get('types', 'contact', 'numbers')
    return render(request, 'edit_contact.html', {'contact': contact, 'types': types})


def add_contact(request):
    if request.method == 'POST':
        name_contact = AddNameContact(request.POST)
        type_contact = AddTypeContact(request.POST)
        if name_contact.is_valid() and type_contact.is_valid():
            name_contact.save()
            type_contact.save()
            return redirect('home')
        else:
            context = {
                'name_contact': name_contact,
                'type_contact': type_contact,
            }
    else:
        context = {
            'name_contact': AddNameContact,
            'type_contact': AddTypeContact,
        }
    return render(request, 'add_contact.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



