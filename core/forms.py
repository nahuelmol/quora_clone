from .models import Users
from django import forms

class users_form(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Users
		fields = ['name','email','password']
