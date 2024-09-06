from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include all CRUD routes for tasks
]
