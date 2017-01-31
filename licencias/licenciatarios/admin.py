from django.contrib import admin
from django.contrib import messages
from django import forms
from django.utils.html import format_html

# Register your models here.
from .models import Licenciatarios

admin.site.register(Licenciatarios)
