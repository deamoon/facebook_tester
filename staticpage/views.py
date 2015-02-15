from django.shortcuts import render
from django.contrib.auth import get_user_model as user_model
from open_facebook.api import OpenFacebook
from datetime import datetime
import requests
from page_test.models import Company, Images
from django.shortcuts import redirect
User = user_model()

def strToDate(date):
    dat, t = date.strip().split()
    y, mon, d = dat.split('/')
    h, m = t.split(':')
    return datetime(int(y), int(mon), int(d), int(h), int(m))

def get_like(token, id_page):
    base_url = 'https://graph.facebook.com/' + id_page
    url = '%s?access_token=%s' % (base_url, token,)
    content = requests.get(url).json()
    return int(content['likes'])

def index_main(request):
    if request.user.is_authenticated():
        try:
            token, id_page, name = request.POST['company'].strip().split('+')            
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
            facebook = OpenFacebook(request.user.access_token)
            context = {
                'footer_not_fix': False,
                'data' : facebook.get('me/accounts')["data"],
                'user' : request.user,
            }
            return render(request, 'staticpage/index_login.html', context)
    else:
        context = {
            'footer_not_fix': True,
        }
        return render(request, 'staticpage/index.html', context)
