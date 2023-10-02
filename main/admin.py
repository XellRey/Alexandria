from django.contrib import admin
from .models import Books, ContactMessage
# Register your models here.

admin.site.register(Books)
admin.site.register(ContactMessage)
