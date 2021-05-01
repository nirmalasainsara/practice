from rest_framework import serializers
from .models import Todo
from django.utils.timezone import now
from datetime import timedelta


class TodoSerializer(serializers.ModelSerializer):
    items_completed_in_last_2_days = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def get_items_completed_in_last_2_days(self, obj):
        date_created = now() - timedelta(days=2)
        return Todo.objects.filter(date_created__gt=date_created).count()
