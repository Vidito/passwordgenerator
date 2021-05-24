from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render (request, 'gen/home.html')

def about(request):
    return render(request, 'gen/about.html')


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length= int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_}{\?/'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    thepassword= ''
    for i in range(length):
        thepassword+= random.choice(characters)

    
    return render(request, 'gen/password.html', {'password': thepassword})