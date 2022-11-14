from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import FullMenu


class MenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullMenu
        fields = ['title', 'description', 'price']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']