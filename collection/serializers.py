from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser, Collection


class CollectionSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'name', 'created_at', 'updated_at', 'owner')
