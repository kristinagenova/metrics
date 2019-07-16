from django.urls import path
from api.views import MetricsView


urlpatterns = [
    path('metrics/', MetricsView.as_view({'post': 'get_metrics_controller'}), name='get_metrics_controller'),
]
