from django import forms
from students.models import Student, Teacher


class StudentForm(forms.ModelForm):
	teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), empty_label='выберите учителя из списка')
	class Meta:
		model = Student
		fields = ('name', 'surname', 'birth_date', 'school', 'grade', 'average_mark', 'teacher', 'photo'

			)


class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ('name', 'surname', 'birth_date', 'school'
			)