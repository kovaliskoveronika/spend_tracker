from django.db.models import Sum
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient

from spend.models import SpendStatistic
from spend.serializers import SpendStatisticSerializer

SPEND_URL = reverse("spend:spendstatistic-list")


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


class SpendTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.spend = sample_spend()

    def test_list_spend_statistics(self):
        response = self.client.get(SPEND_URL)

        self.assertEqual(response.status_code, 200)

        data_db = SpendStatistic.objects.values("name", "date").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Sum("revenues__revenue")
        )
        serializer = SpendStatisticSerializer(data_db, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_spend_statistic(self):
        new_spend_data = {
            "name": "Test Name",
            "date": "2023-09-16",
            "spend": 10.0,
            "impressions": 1.0,
            "clicks": 1,
            "conversion": 1
        }

        response = self.client.post(SPEND_URL, new_spend_data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(SpendStatistic.objects.filter(name="Test Name").exists())
