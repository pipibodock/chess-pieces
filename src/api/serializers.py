from rest_framework import serializers

from pieces.models import Pieces


class PiecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieces
        fields = ['name', 'color']

    def create(self, validated_data):
        piece = Pieces.objects.create(**validated_data)
        return piece

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
