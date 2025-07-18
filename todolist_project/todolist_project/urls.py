from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Handles frontend + API both
    path('api-auth/', include('rest_framework.urls')),  # Optional login for browsable API
]
