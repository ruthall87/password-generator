from django.http.response import HttpResponse
from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list("abcdefghijklmnopqrdtuvwxyz")
    length = int(request.GET.get("length", 12))
    thepassword = ""
    
    if request.GET.get("uppercase"):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get("special"):
        characters.extend(list('!@#$%^&**(()_-'))
    if request.GET.get("number"):
        characters.extend(list('1234567891011121314145116171891'))

        for x in range(length):
            thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


# Create your views here.
