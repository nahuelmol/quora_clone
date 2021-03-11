from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login

from .models import Users
from .forms import users_form

def main(req):
	return HttpResponse('Hola')

class registerPage(View):
	def get(self,request):
		form  = users_form()
		content = {'form':form}
		
		template = 'core/users_form.html'
		return render(request, template, content)

	def post(self,request):
		form = users_form(request.POST, request.FILES or None)
		#
		if form.is_valid():
			user = form.save(commit=False)
			

			user.password= make_password(form.cleaned_data.get('password'))
			user.save()
			print(user)

			return redirect(reverse('core:main_url'))

		content = {'form':form}
		template = 'core/users_form.html'

		return render(request, template, content)




