from django.shortcuts import render
from django.http import HttpResponse
import json
from models import Company, Images
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import get_object_or_404
import requests

def strToDate(date):
    dat, t = date.strip().split()
    y, mon, d = dat.split('/')
    h, m = t.split(':')
    return datetime(int(y), int(mon), int(d), int(h), int(m))

@login_required
def detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    try:
        photos_datas = request.POST.getlist('multiple')
        request.POST['multiple']

        for i, photo_data in enumerate(photos_datas):
            photo_id, photo_source = photo_data.split('+')
            image = Images(number=i, company=company, id_photo=photo_id, source=photo_source)
            image.save()
        company.level = 1
        company.save()
        return redirect('/page_test')
    except KeyError:
        if company.level == 0:
            base_url = 'https://graph.facebook.com/' + company.id_page + '/photos/uploaded'
            url = '%s?access_token=%s' % (base_url, company.token,)

            content = requests.get(url).json()
            
            context = {
                'user' : request.user,
                'company' : company,
                'data' : content["data"],
                'url' : url,
            }

            return render(request, 'page_test/detail.html', context)
        else:
            images = Images.objects.filter(company=company_id)
            context = {
                'data' : images,
            }
            return render(request, 'page_test/result.html', context)

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
        # start = request.POST['start']
        end = request.POST['end']

        company = Company(token=token, id_page=id_page, user=request.user, name=name, 
                          start=datetime.now(),
                          end=strToDate(end),
                          level=0,
                         )
        company.save()
        return redirect('/page_test')
    except KeyError:
        return render(request, 'page_test/add.html')