from django.urls import path
from .views import student_list, student_detail, student_create, teacher_create



urlpatterns = [
    path('student', student_list, name = "student_list"),
    path('student/<int:student_id>', student_detail, name='student_detail'),
    path('student_create', student_create, name='student_create'),
    path('teacher_create', teacher_create, name='teacher_create')
    

]
