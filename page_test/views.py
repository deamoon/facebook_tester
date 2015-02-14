from django.shortcuts import render
from django.http import HttpResponse
import json
from models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def detail(request, company_id):


@login_required
def index(request):
    context = {
        'user' : request.user,
        'companys' : Company.objects.filter(user__id=request.user.id),
        'id' : request.user.id,
    }
    
    return render(request, 'page_test/2.html', context)

@login_required
def add(request):
    try:
        token = request.POST['token']
        id_page = request.POST['id_page']
        name = request.POST['name']        
        company = Company(token=token, id_page=id_page, user=request.user, name=name)
        company.save()
        return redirect('/page_test')
    except KeyError:
        return render(request, 'page_test/1.html')