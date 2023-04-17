from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class DateInput(forms.DateInput):
	input_type = 'date'

class CreateUserForm(UserCreationForm):
	dob = forms.DateField(widget=DateInput,required=True)

	class Meta:
		model = User
		fields = ['username', 'email','dob', 'password1', 'password2']
