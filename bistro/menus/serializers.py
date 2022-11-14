from django.contrib.auth.models import menus, Group
from rest_framework import serializers


class MenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menus
        fields = ['title', 'description', 'price']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']git ad