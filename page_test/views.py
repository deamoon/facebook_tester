from django.shortcuts import render
from django.http import HttpResponse
import json
from models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime

def strToDate(date):
    dat, t = date.strip().split()
    y, mon, d = dat.split('/')
    h, m = t.split(':')
    return datetime(int(y), int(mon), int(d), int(h), int(m))

@login_required
def detail(request, company_id):
    # if (company_id == request.user.id):
    context = {
        'user' : request.user,
    }
    return render(request, 'page_test/detail.html', context)

@login_required
def index(request):
    context = {
        'user' : request.user,
        'companys' : Company.objects.filter(user__id=request.user.id),
        'id' : request.user.id,
    }
    return render(request, 'page_test/main.html', context)

@login_required
def add(request):
    try:
        token = request.POST['token']
        id_page = request.POST['id_page']
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']

        company = Company(token=token, id_page=id_page, user=request.user, name=name, 
                          start=strToDate(start),
                          end=strToDate(end),
                         )
        company.save()
        return redirect('/page_test')
    except KeyError:
        return render(request, 'page_test/add.html')