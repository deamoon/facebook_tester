from django.contrib import admin
from django.contrib.auth import get_user_model as user_model
User = user_model()
admin.site.register(User)