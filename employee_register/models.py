from django.db import models

# Create your models here.

class Position(models.Model):
	title = models.CharField(max_length = 100)

	def __str__ (self):
		return self.title

class Department(models.Model):
	department = models.CharField(max_length = 100)

	def __str__(self):
		return self.department
	
class Employee(models.Model):
	fullname = models.CharField(max_length = 100)
	emp_code = models.CharField(max_length = 3)
	mobile = models.CharField(max_length = 10)
	position = models.ForeignKey(Position, on_delete = models.CASCADE)
	department = models.ForeignKey(Department, on_delete = models.CASCADE)

