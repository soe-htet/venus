from django.contrib import admin

# Register your models here.

from .models import EmailConfirmed

admin.site.register(EmailConfirmed)