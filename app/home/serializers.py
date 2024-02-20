from rest_framework import serializers
from .models import PlantedTree

class PlantedTreeSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = PlantedTree
        fields = ['id', 'longitude', 'longitude', 'user_name']

    def get_user_name(self, obj):

        return obj.user.username if obj.user else None
