from django.urls import include, path
from rest_framework.routers import DefaultRouter

from photos.api import views as qv

router = DefaultRouter()
router.register(r"photos", qv.PhotoViewSet)

urlpatterns = [
    path("", include(router.urls))
]