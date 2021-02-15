from django.urls import include, path
from rest_framework.routers import DefaultRouter

from photos.api import views as qv

router = DefaultRouter()
router.register(r"photos", qv.PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("photos/<int:pk>/comments/", qv.CommentListAPIView.as_view(), name="comment-list"),
    path("photos/<int:pk>/comment/", qv.CommentCreateAPIView.as_view(), name='comment-create'),
    path("photos/<int:pk>/like/", qv.PhotoLikeAPIView.as_view(), name="photo-like"),
    path("comments/<int:pk>/", qv.CommentRUDAPIView.as_view(), name="comment-detail"),
]
