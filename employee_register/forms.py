from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('emp_code', 'fullname', 'department', 'position', 'mobile')
		labels = {
			'fullname' : 'Full Name',
			'emp_code' : 'Employee Code',
			'department' : 'Department',
			'position' : 'Position',
			'mobile' : 'Mobile'

		}

		def __init__(self, *args, **kwargs):
			super(EmployeeForm, self).__init__(*args, **kwargs)
			self.fields["position"].empty_label = "Select position"
			self.fields["department"].empty_label = "Select department"
			self.fields["emp_code"].required = false