import django.http
from django.shortcuts import render


def home(request: django.http.HttpRequest):
    return render(request, 'home.html')


def reverse(request: django.http.HttpRequest):
    print(type(request.GET))
    user_text = request.GET['user-text']
    print(user_text)
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text})
