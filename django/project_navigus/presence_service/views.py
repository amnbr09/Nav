from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello. Welcome to Doc Presence Service")
# Create your views here.
