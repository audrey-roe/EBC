from django.contrib import admin
from .models import wamessage_log, rec_numbers,test

# Register your models here.
admin.site.register(wamessage_log)
admin.site.register(rec_numbers)
admin.site.register(test)