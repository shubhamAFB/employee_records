from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
	if request.method == "GET":
		employees = Employee.objects.all()
		return render(request, "employee_register/employeelist.html", {'employees' : employees})

def employee_form(request, id = 0):
	if request.method == "GET":
		if id == 0:			
			form = EmployeeForm()
			return render(request, "employee_register/employeeform.html", {'form' : form})
		else:
			employee = Employee.objects.get(pk = id)
			form = EmployeeForm(instance = employee)
			return render(request, "employee_register/employeeform.html", {'form' : form})
	elif request.method == "POST":
		if id == 0:
			form = EmployeeForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect ("/list")
		else:
			employee = Employee.objects.get(pk = id)
			form  = EmployeeForm(request.POST, instance = employee)
			if form.is_valid():
				form.save()
				return redirect("/list/")
	

def employee_delete(request, id):
	employee = Employee.objects.get(pk = id)
	employee.delete()
	return redirect("/list/")
