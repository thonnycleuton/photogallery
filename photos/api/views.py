from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from photos.api.permissions import IsAuthorOrReadOnly
from photos.api.serializers import PhotoSerializer, CommentSerializer
from photos.models import Photo, Comment


class PhotoViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Question."""
    queryset = Photo.objects.all().order_by("-created_at")
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PhotoLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        photo = get_object_or_404(Photo, pk=pk)
        user = request.user

        photo.voters.add(user)
        photo.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(photo, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        photo = get_object_or_404(Photo, pk=pk)
        user = request.user

        photo.voters.remove(user)
        photo.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(photo, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        pk = self.kwargs.get('pk')
        photo = get_object_or_404(Photo, pk=pk)
        serializer.save(author=request_user, photo=photo)


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an answer instance to it's author."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CommentListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(photo_id=pk).order_by("-created_at")
