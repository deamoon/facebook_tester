from django.shortcuts import render
from django.shortcuts import redirect

def profile(request):
    context = {
        'name_user': "dima",
    }
    return render(request, 'user_profile/profile.html', context)

def main(request):
    return redirect('/page_test')
