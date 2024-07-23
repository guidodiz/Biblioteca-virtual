from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
	return render(request, 'web/index.html')

def forms(request):
	context={
		'form': None
	}
	return render(request, 'web/forms.html', context)