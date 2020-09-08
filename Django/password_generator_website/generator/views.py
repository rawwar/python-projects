from django.shortcuts import render
import string
from random import choice
# Create your views here.


def password_generate(request):
    return render(request, 'generator/password_generator.html')


def show_password(request):
    tokens = string.ascii_lowercase
    if 'uppercase' in request.GET:
        tokens += string.ascii_uppercase
    if 'numbers' in request.GET:
        tokens += string.digits
    if 'specialCharacters' in request.GET:
        tokens += "!@#$%^&*()_-+="
    password_length = int(request.GET['password_length'])
    password = "".join([choice(tokens) for i in range(password_length)])
    return render(request, 'generator/show_password.html',{"password":password})