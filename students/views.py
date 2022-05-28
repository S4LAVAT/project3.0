from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm 



def student_list(request):
	students = Student.objects.all()
	search_query = request.GET.get('q', '')
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


def teachers_list(request):
	teachers = Teacher.objects.all()
	search_query = request.GET.get('q', '')
	if search_query:
		teachers = teachers.filter(name__contains=search_query)
	context ={
		'teachers':teachers,
		'search_query':search_query,
	}
	return render(request, 'students/teachers_list.html', context)


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





def student_update(request, student_id):
	student = get_object_or_404(Student,id=student_id)
	form = StudentForm(request.POST or None, instance=student)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)

	context = {'form': form}
	return render(request, 'students/student_update.html', context)




def student_delete(request, student_id):
	student = get_object_or_404(Student,id=student_id)
	if request.method == 'POST':
		student.delete()
		return redirect('student_list')
	context = {
		'student':student
	}
	return render(request, 'students/student_delete.html', context)




def teacher_filter(request):
	teacher = Teacher.object.get(name)
	student = Student.object.filter(teacher = teacher)
	return 



def teacher_filter(request, student_id):
	teacher = Teacher.object.get(id = teacher.id)
	student = Student.object.filter(teacher = teacher)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)

	context = {'form': form}
	return render(request, 'students/teacher_filter.html', context)


 




 






