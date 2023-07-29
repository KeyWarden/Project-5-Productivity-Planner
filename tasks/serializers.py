from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """serializes the Task data"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'due_at',
            'title', 'description', 'is_owner'
        ]
