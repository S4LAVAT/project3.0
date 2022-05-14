
from django.urls import path
from .views import student_list, student_detai



urlpatterns = [
    path('student', student_list, name = "student_list"),
    path('student/<int:student_id>', student_detail, name='student_detail')
    

]
