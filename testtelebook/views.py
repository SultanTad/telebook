from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django_filters.views import FilterView
from django.views.generic import UpdateView

from .models import *
from .forms import AddNameContact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .filters import TeleBookFilter


class FilterList(FilterView):
    model = ContactInPhone
    filterset_class = TeleBookFilter
    template_name = 'index.html'


def edit_contact(request):
    contact = ContactInPhone.objects.all()
    return render(request, 'edit_contact.html', {'contact': contact})


def update_contact(request, pk):
    get_contact = ContactInPhone.objects.get(pk=pk)
    update = True

    if request.method == 'POST':
        form = AddNameContact(request.POST, instance=get_contact)
        if form.is_valid():
            form.save()
            return redirect('edit_contact')

    form = AddNameContact(instance=get_contact)
    return render(request, 'edit_contact.html', {'form': form, 'get_contact': get_contact, 'update': update})


def delete_contact(request, pk):
    get_phone = ContactInPhone.objects.get(pk=pk)
    get_phone.delete()
    return redirect(reverse('edit_contact'))


def add_contact(request):
    if request.method == 'POST':
        name_contact = AddNameContact(request.POST)
        if name_contact.is_valid():
            name_contact.save()
            return redirect('home')
        else:
            context = {
                'name_contact': name_contact,
            }
    else:
        context = {
            'name_contact': AddNameContact,
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



