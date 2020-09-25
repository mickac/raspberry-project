from rest_framework import serializers
from .models import PeopleList

class PeopleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleList
        fields = ('id', 'name', 'email', 'info')