from django.urls import path, include
from rest_framework import routers

from .views import SpendViewSet

router = routers.DefaultRouter()
router.register("spend-statistic", SpendViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "spend"
