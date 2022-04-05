from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('test/', views.Test.as_view(), name='test'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]