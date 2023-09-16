from rest_framework import serializers

from spend.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ("id", "name", "date", "spend", "impressions", "clicks", "conversion")


class SpendStatisticSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_impressions = serializers.IntegerField(default=0)
    total_clicks = serializers.IntegerField(default=0)
    total_conversion = serializers.IntegerField(default=0)
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)

