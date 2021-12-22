from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

urlpatterns = [
    #path('api/',views.article_list, name='api'),
    path('api/',views.ArticleAPI.as_view(), name='api'),

    path('generic/api/<int:pk>/',views.GenericAPIView.as_view(), name='generic'),

    path('detail/<int:pk>/', views.ArticleDetail.as_view(), name='deatil')
]