from django.urls import path
from . import views

# Общее простраство имен
app_name = 'blog'

# Пути/ссылки приложения blog
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_posts, name='category_posts'),
]
