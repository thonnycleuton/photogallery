from rest_framework import serializers
from photos.models import Photo, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["photo", "updated_at"]
