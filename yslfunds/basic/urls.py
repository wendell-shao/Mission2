from django.urls import path, re_path

from . import views

urlpatterns = [
    # /article/
    path('', views.articles, name='article'),
    # /article/article_id
    path('content/', views.content, name='content'),
]