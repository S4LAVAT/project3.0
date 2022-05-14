from django.shortcuts import render
from .models import Student

def student_list(request):
	student = Student.object.all()
	context ={
		'student':student
	}
	return render(request, 'app/student_list.html', context)


def student_detail(request):
	student = Student.object.all()
	context ={
		'student':student
	}
	return render(request, 'app/student_detail.html', context)


