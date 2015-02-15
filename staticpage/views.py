from django.shortcuts import render
from django.contrib.auth import get_user_model as user_model
from open_facebook.api import OpenFacebook
User = user_model()

def index_main(request):
    if request.user.is_authenticated():
        facebook = OpenFacebook(request.user.access_token)
        context = {
            'footer_not_fix': False,
            'data' : facebook.get('me/accounts')["data"],
        }
        return render(request, 'staticpage/index_login.html', context)
    else:
        context = {
            'footer_not_fix': True,
        }
        return render(request, 'staticpage/index.html', context)
