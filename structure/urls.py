from django.urls import path
from . import views

app_name = 'structure'

urlpatterns = [
    path('academic-year/', views.academic_year, name='academic_year'),
    path('academic-year//<int:pk>/delete/', views.academic_year_delete, name='academic_year_delete'),
    path('academic-year//<int:pk>/detail/', views.academic_year_detail, name='academic_year_detail'),
    path('academic-year//<int:pk>/update/', views.academic_year_update, name='academic_year_update'),
    path('academic-year//create/', views.academic_year_create, name='academic_year_create'),

    path('kafedra/', views.kafedra_list, name='kafedra_list'),
    path('kafedra//<int:pk>/delete/', views.kafedra_delete, name='kafedra_delete'),
    path('kafedra//<int:pk>/detail/', views.kafedra_detail, name='kafedra_detail'),
    path('kafedra//<int:pk>/update/', views.kafedra_update, name='kafedra_update'),
    path('kafedra//create/', views.kafedra_create, name='kafedra_create'),

    path('lesson-time/', views.lesson_time_list, name='lesson_time_list'),
    path('lesson-time//<int:pk>/delete/', views.lesson_time_delete, name='lesson_time_delete'),
    path('lesson-time//<int:pk>/detail/', views.lesson_time_detail, name='lesson_time_detail'),
    path('lesson-time//<int:pk>/update/', views.lesson_time_update, name='lesson_time_update'),
    path('lesson-time//create/', views.lesson_time_create, name='lesson_time_create'),
]