from django.db.models import Sum
from rest_framework import viewsets, mixins

from .serializers import SpendSerializer, SpendStatisticSerializer
from .models import SpendStatistic


class SpendViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = SpendStatistic.objects.values("name", "date").annotate(
        total_spend=Sum("spend"),
        total_impressions=Sum("impressions"),
        total_clicks=Sum("clicks"),
        total_conversion=Sum("conversion"),
        total_revenue=Sum("revenues__revenue")
    )
    serializer_class = SpendSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return SpendStatisticSerializer
        return SpendSerializer
