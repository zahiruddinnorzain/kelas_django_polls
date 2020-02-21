from django.shortcuts import render, redirect
from register.models import Register

def index(request):
	context = {
		'posts': Register.objects.all()
	}
	return render(request, 'undi/profile.html', context)