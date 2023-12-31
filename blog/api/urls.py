from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users//', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts//', views.PostDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

