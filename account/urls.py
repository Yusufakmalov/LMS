from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('users-list/', views.users_list, name='users_list'),
    path('user-detail/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
]