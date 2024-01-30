from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('posts/', BlogPostListView.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
]