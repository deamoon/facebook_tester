from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'page_test/1.html')
