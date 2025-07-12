from django.contrib import admin
from .models import Task  # 👈 make sure this is correct

admin.site.register(Task)  # 👈 this line registers the model
