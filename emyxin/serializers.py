from rest_framework import serializers
from emyxin.models import checkinlist


class CheckinlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = checkinlist

        fields = ['title', 'singner','created_time']