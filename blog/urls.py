from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    #  path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #path for individual post
    path('post/new/', PostCreateView.as_view(), name='post-create'), #path for new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #path for individual post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), #path for individual post
    path('about/', views.about, name='blog-about'),
] 