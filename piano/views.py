from django.shortcuts import render
from django.http import HttpResponse
from models import Piano
import json

def index(request):
    return render(request, 'piano/piano.html')

def play(request):
    if (request.GET['note']):
        note = Piano(note = int(request.GET['note']))    
        note.save()
    return HttpResponse('')

def get(request):
    last_ten = Piano.objects.all().order_by('-id')[:30]
    last_ten_in_ascending_order = reversed(last_ten)
    list_notes = []
    for data in last_ten_in_ascending_order:
        list_notes.append((data.id, data.note))
    return HttpResponse(json.dumps(list_notes), content_type="application/json")