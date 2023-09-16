from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = ("id", "name", "spend", "date", "revenue")


class RevenueStatisticSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_impressions = serializers.IntegerField(default=0)
    total_clicks = serializers.IntegerField(default=0)
    total_conversion = serializers.IntegerField(default=0)
