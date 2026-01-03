from django.urls import path
from .views import *

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_create, name='student_add'),
    path('edit/<int:id>/', student_update, name='student_edit'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
]
