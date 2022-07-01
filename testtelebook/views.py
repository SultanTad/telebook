from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Phone
from .forms import AddForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class TeleView(ListView):
    model = Phone
    template_name = 'index.html'
    queryset = Phone.objects.all()


class TeleSearch(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Phone.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context


def add_contact(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            Phone.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = AddForm()
    return render(request, 'add_contact.html', {'form': form})


def delete_contact(request, pk):
    get_phone = Phone.objects.get(pk=pk)
    get_phone.delete()
    return redirect(reverse('home'))


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









