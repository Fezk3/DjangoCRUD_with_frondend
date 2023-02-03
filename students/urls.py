from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>', views.student_details, name='student_details'),
    path('delete/<int:student_id>', views.student_delete, name='student_delete'),
    path('add', views.add_student, name='add_student'),
    path('edit/<int:student_id>', views.edit_student, name='edit_student'),
]
