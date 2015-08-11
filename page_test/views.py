from django.shortcuts import render
from django.http import HttpResponse
import json
from models import Company, Images
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import get_object_or_404
import requests
from page_test.facebook import *
import logging

logger = logging.getLogger('page_test')

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
            if i == 0:
                company.current_photo_id = image.id
                set_cover(company.user, company, image)
        company.level = 1
        company.number_photos = len(photos_datas)
        company.save()
        return redirect('/page_test')
    except KeyError:
        if company.level == 0:
            if not company.album_cover:
                album = get_album_cover(company.token, company.id_page)
                if album:
                    company.album_cover = album
                company.save()

            if company.album_cover:
                base_url = 'https://graph.facebook.com/' + company.album_cover + '/photos'
                url = '%s?access_token=%s' % (base_url, company.token,)
                content = requests.get(url).json()
                logger.info(url, content)
            else:
                content = {'data':[]}

            context = {
                'user' : request.user,
                'company' : company,
                'data' : content["data"],
            }

            return render(request, 'page_test/detail.html', context)
        else:
            images = Images.objects.filter(company=company_id)
            max_likes = max([image.likes for image in images])
            data = []
            for image in images:
                if max_likes != 0:
                    length = int(image.likes * 500 / max_likes)
                else:
                    length = 0
                data.append({
                    'source' : image.source,
                    'len' : length,
                    'likes' : image.likes
                })
            context = {
                'data' : data,
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
        likes = get_like(token, id_page)
        company = Company(token=token, id_page=id_page, user=request.user, name=name,
                          start=datetime.now(),
                          end=strToDate(end),
                          level=0,
                          number_photos=0,
                          current_photo_id=0,
                          likes=likes,
                         )
        company.save()
        return redirect('/page_test')
    except KeyError:
        return render(request, 'page_test/add.html')