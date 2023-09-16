from django.urls import path, include
from rest_framework import routers

from .views import RevenueViewSet

router = routers.DefaultRouter()
router.register("revenue-statistic", RevenueViewSet)

urlpatterns = [
    path("", include(router.urls))]

app_name = "revenue"
