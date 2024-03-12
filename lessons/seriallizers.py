from rest_framework import serializers
from lessons.models import Lesson
#
# class FruitSerializer(serializers.Serializer):
#     id = serializers.UUIDField()
#     name = serializers.CharField()
#     price = serializers.IntegerField()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'subject',
            'plan',
        )