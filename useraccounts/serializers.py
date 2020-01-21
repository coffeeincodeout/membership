from django.contrib.auth.models import User, Group
from .models import Members
from rest_framework import serializers


class MembersSerializer(serializers.ModelSerializer):
    data = serializers.DictField()
    class Meta:
        model = Members
        fields = ['pk', 'data']
