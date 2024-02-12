from django.shortcuts import render, redirect
from .models import Category, Movie
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.db import IntegrityError


# Create your views here.

# Основная страница
def home(request):
    # Поисковая строка
    search_bar = forms.SearchForm()
    # Получение всех категорий
    category = Category.objects.all()
    # Получение всех фильмов
    movie = Movie.objects.all()
    context = {
        'form': search_bar,
        'category': category,
        'movie': movie
    }
    return render(request, 'home.html', context)


# Получение информации о категориях
def exact_category(request, pk):
    all_category = Category.objects.get(id=pk)
    movies = Movie.objects.filter(category=all_category)
    context = {
        'movies': movies,
        'category': all_category
    }
    return render(request, 'category.html', context)


# Получение информации о фильмах
def exact_movie(request, pk):
    # Получения всех фильмов
    all_movie = Movie.objects.get(id=pk)
    context = {
        'movie': all_movie
    }
    return render(request, 'movie.html', context)


# Поиск фильмов
def search_engine(request):
    if request.method == 'POST':
        get_movie = request.POST.get('search_engine')
        try:
            specific_movie = Movie.objects.get(name__icontains=get_movie)
            return redirect(f'/movie/{specific_movie.id}')
        except:
            return redirect('/error')


# Страница ошибки
def error(request):
    return render(request, 'error.html')


# Функция для logout
def logout_view(request):
    logout(request)
    return redirect('/')


# Для регистрации пользователя или входа в их аккаунт
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Проверка пользователя в базе
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html',
                          {'error': 'Хм! Я думаю вы уже зарегистрированы. Попробуйте войти!'})

        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user)
            authenticated_user = authenticate(request, username=username, password=password)
            login(request, authenticated_user)
            return redirect('/')
        except IntegrityError:
            return render(request, 'registration/register.html',
                          {'error': 'Данные введены неправильно! Попробуйте ещё раз!'})
    return render(request, 'registration/register.html')
