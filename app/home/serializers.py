from rest_framework import serializers
from .models import PlantedTree

class PlantedTreeSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = PlantedTree
        fields = ['id', 'longitude', 'longitude', 'user_name']  # Add other fields as necessary

    def get_user_name(self, obj):
        # Retorna o nome do usuário associado à árvore plantada
        return obj.user.username if obj.user else None
