from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet
from .views import frontend

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', frontend, name='frontend'),
    path('api/', include(router.urls)),  # GET/POST/PATCH/DELETE via /api/tasks/
]
