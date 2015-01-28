from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from .models import Light
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')

def light(request):
	response_data = []
	light_data = Light.objects.all()
	for data in light_data:
		dict_data = {
			'light_id' : data.id,
			'light_level' : data.level
		}
		response_data.append(dict_data)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

# def light_edit(request):
	

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

