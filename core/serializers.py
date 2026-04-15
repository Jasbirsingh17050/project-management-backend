from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Project, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "created_at"]
        read_only_fields = ["created_at"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "project",
            "assigned_to",
            "created_at",
        ]
        read_only_fields = ["created_at"]

    def validate_status(self, value):
        valid_statuses = ["pending", "in-progress", "completed"]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Status must be one of: pending, in-progress, completed"
            )
        return value