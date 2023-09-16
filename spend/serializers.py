from rest_framework import serializers

from spend.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ("id", "name", "date", "spend", "impressions", "clicks", "conversion")
