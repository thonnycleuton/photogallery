from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from photos.api.permissions import IsAuthorOrReadOnly
from photos.api.serializers import PhotoSerializer
from photos.models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Question."""
    queryset = Photo.objects.all().order_by("-created_at")
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
