from django.urls import path
from . import views

# Для контроля ссылок
urlpatterns = [
    # path('login/', views.login_page),
    path('', views.home),
    path('movie/<int:pk>', views.exact_movie),
    path('category/<int:pk>', views.exact_category),
    # path('register', views.Register.as_view()),
    path('register', views.register, name='register'),
    path('accounts/logout/', views.logout_view),
    path('search', views.search_engine),
    path('error', views.error),
]
