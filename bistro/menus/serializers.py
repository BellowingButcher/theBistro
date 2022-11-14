from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import FullMenu, SPICY_LEVEL_CHOICES

class FullMenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.IntegerField(read_only=True)
    spicy_level = serializers.ChoiceField(choices=SPICY_LEVEL_CHOICES, default=1)

    def create(self, validated_data):
        """
        Create and return a new `menu` instance, given the validated data.
        """
        return menus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `menu` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.code)
        instance.price = validated_data.get('price', instance.linenos)
        instance.spicy_level = validated_data.get('spicy_level', instance.language)
        instance.save()
        return instance


class MenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullMenu
        fields = ['title', 'description', 'price']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']