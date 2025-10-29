# 配置URL

from django.urls import path
from .views import GoodDeedListCreateView

urlpatterns = [
    path('gooddeeds/', GoodDeedListCreateView.as_view(), name='gooddeeds-list'),
]