from rest_framework import serializers

from .models import Person


class StarwarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('title', 'cat_id')