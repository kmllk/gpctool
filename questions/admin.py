from django.contrib import admin

# Register your models here.
from .models import Question_schema

admin.site.register(Question_schema)
