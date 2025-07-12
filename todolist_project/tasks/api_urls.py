from rest_framework.routers import DefaultRouter
from .views import TaskViewSet  # ✅ now it works

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
