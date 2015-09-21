from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Division)
admin.site.register(League)
