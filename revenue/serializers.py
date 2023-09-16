from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = ("id", "name", "spend", "date", "revenue")
