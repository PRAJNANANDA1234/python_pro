from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def java(request):
    return HttpResponse('<h1>statically type language</h1>')