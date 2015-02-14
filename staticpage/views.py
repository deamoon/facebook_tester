from django.shortcuts import render

def index_main(request):
    if request.user.is_authenticated():
        context = {
            'footer_not_fix': False,
        }
        return render(request, 'staticpage/index_login.html', context)
    else:
        context = {
            'footer_not_fix': True,
        }
        return render(request, 'staticpage/index.html', context)
