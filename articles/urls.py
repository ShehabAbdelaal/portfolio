#Define URL patterns for articles

from django.urls import path, include
from . import views

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    #show all articles
    path('articles', views.articles, name = 'articles'),
    path('articles/<int:article_id>/', views.article_detail, name='detail')
]