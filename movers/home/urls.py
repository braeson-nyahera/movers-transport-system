from django.urls import path
from home import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/',PostListView.as_view(), name='home'),
    path('post/<pk>',PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('about', views.about, name='about'),
    path('', views.landing, name='landing_page'),
]