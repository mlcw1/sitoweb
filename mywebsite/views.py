from django.shortcuts import render

# Create your views here.

def mywebsite(request):
	return render (request, 'mywebsite/sitowebmlc.html')

def about(request):
	return render (request, 'mywebsite/about.html')

def skills(request):
	return render (request, 'mywebsite/skills.html')

def education(request):
	return render (request, 'mywebsite/education.html')

def experience(request):
	return render (request, 'mywebsite/experience.html')

def master(request):
	return render (request, 'mywebsite/master.html')

def contact(request):
	return render (request, 'mywebsite/contact.html')
