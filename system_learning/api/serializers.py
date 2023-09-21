from rest_framework import serializers

from products.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "title", "video_url", "duration_seconds")
