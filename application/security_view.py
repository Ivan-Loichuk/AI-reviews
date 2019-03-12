from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.parsers import JSONParser


def registration(request):
    data = JSONParser().parse(request)
    user = User.objects.create_user(data['username'], data['email'], data['password'])
    user.last_name = data['lastname']
    try:
        user.save()
    except:
        return HttpResponse('Failed to create user: ' + data['username'], status=500)
    return HttpResponse('Success', status=201)


def auth(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('Successful authorization', status=200)
    else:
        return HttpResponse('Failed to log in', status=401)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('')
