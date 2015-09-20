from django.contrib import admin

# Register your models here.
from .models import League
from .models import Division
from .models import Account
from .models import Notification

admin.site.register(League)
admin.site.register(Division)
admin.site.register(Account)
admin.site.register(Notification)

