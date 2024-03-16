from django.urls import path
from home import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('', views.landing, name='landing_page'),
]
