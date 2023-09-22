from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("its my first django app on windows using docker")
