from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm



def student_list(request):
	students = Student.objects.all()
	search_query = request.GET.get('q')
	grade_query = request.GET.get('grade')
	if search_query:
		students = students.filter(name__contains=search_query)
	if grade_query:
		students = students.filter(grade=grade_query)
	context ={
		'students':students,
		'search_query':search_query,
		'grade_query':grade_query
	}
	return render(request, 'students/student_list.html', context)


def student_detail(request, student_id):
	#student = Student.objects.get(id=student_id)
	student = get_object_or_404(Student, id=student_id)
	context ={
		'student':student
	}
	return render(request, 'students/student_detail.html', context)


def student_create(request):
	form = StudentForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)

	context = {'form': form}
	return render(request, 'students/student_create.html', context)




def teacher_create(request):
	form = TeacherForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)

	context = {'form': form}
	return render(request, 'students/teacher_create.html', context)


