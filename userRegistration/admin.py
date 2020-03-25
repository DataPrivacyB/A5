from django.contrib import admin
from .models import Profile,SharesHeld,Shares

admin.site.register(Profile)
# Register your models here.
admin.site.register(SharesHeld)
admin.site.register(Shares)