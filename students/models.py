
from django.db import models 

class Student(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	birth_date = models.DateField()
	grade = models.IntegerField()
	average_mark = models.DecimalField(decimal_places=1, max_digits=2)
	photo = models.ImageField(upload_to='cover', null=True, blank=True) 
	school = models.CharField(max_length=300)


	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	birth_date = models.DateField()
	school = models.CharField(max_length=300)


	def __str__(self):
		return self.name
		





	