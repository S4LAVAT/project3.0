from django.urls import path
from .views import student_list, teachers_list, student_detail, student_create, teacher_create, student_update



urlpatterns = [
    path('students', student_list, name = "student_list"),
    path('teachers', teachers_list, name = "teachers_list"),
    path('student/<int:student_id>', student_detail, name='student_detail'),
    path('student_create', student_create, name='student_create'),
    path('teacher_create', teacher_create, name='teacher_create'),
    path('student_update/<int:student_id>', student_update, name='student_update'),
    

]
