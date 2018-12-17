from django.urls import path
from . import views

urlpatterns=[
    path('', views.hola, name='hola'),
    path('link/', views.link, name='link'),
    path('trans/', views.trans, name='trans')
]