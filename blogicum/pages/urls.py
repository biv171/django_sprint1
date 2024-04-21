from django.urls import path
from . import views

# Общее простраство имен
app_name = 'pages'

# Пути/ссылки приложения blog
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
