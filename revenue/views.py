from django.db.models import Sum
from rest_framework import viewsets, mixins

from revenue.models import RevenueStatistic
from revenue.serializers import RevenueSerializer, RevenueStatisticSerializer


class RevenueViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = RevenueStatistic.objects.values("date", "name").annotate(
        total_revenue=Sum("revenue"),
        total_spend=Sum("spend__spend"),
        total_impressions=Sum("spend__impressions"),
        total_clicks=Sum("spend__clicks"),
        total_conversion=Sum("spend__conversion"),
    )
    serializer_class = RevenueSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return RevenueStatisticSerializer
        return RevenueSerializer
