from django.shortcuts import render

def profile(request):
    context = {
        'name_user': "dima",
    }
    return render(request, 'user_profile/profile.html', context)
