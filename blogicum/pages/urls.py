from . import views
from django.urls import path

# Общее простраство имен
app_name = 'pages'

# Пути/ссылки приложения blog
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
