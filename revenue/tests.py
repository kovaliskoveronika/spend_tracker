from django.db.models import Sum
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from revenue.serializers import RevenueStatisticSerializer

REVENUE_URL = reverse("revenue:revenuestatistic-list")


def sample_spend(**params):
    defaults = {
        "name": "Sample revenue",
        "date": timezone.now().date(),
        "spend": 10.0,
        "impressions": 1.0,
        "clicks": 1,
        "conversion": 1
    }
    defaults.update(params)

    return SpendStatistic.objects.create(**defaults)


def sample_revenue(**params):
    defaults = {
        "name": "Sample revenue",
        "spend": sample_spend(),
        "date": timezone.now().date(),
        "revenue": 10.0,
    }
    defaults.update(params)

    return RevenueStatistic.objects.create(**defaults)


class RevenueTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.spend = sample_spend()
        self.revenue = sample_revenue(spend=self.spend)

    def test_list_revenue_statistics(self):
        response = self.client.get(REVENUE_URL)

        self.assertEqual(response.status_code, 200)

        data = response.data

        data_db = RevenueStatistic.objects.values("date", "name").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion"),
        )
        serializer = RevenueStatisticSerializer(data_db, many=True)
        self.assertEqual(data, serializer.data)

    def test_create_revenue_statistic(self):
        new_revenue_data = {
            "name": "Test Name",
            "date": "2023-09-16",
            "revenue": 100.0,
        }

        response = self.client.post(REVENUE_URL, new_revenue_data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(RevenueStatistic.objects.filter(name="Test Name").exists())
