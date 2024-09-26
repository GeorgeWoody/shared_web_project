from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Proyecto subido a GitHub - app Polls")