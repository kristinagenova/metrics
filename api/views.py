from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Metrics
from api.serializers import MetricsSerializer
from api.services import MetricsService


class MetricsView(viewsets.ViewSet):

    @action(detail=True, methods=["post"])
    def get_metrics_controller(self, request):
        serializer = MetricsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            service = MetricsService()

            group_by = data["group"]
            show = service.convert_show_values(data["show"])
            sort = "{0}{1}".format(data["sort"]["order"], data["sort"]["field"])
            filters = service.convert_filter_values(data["filter"])

            metrics_model = Metrics()
            result = metrics_model.get_metrics_from_db(group_by=group_by, show=show, filters=filters, sort=sort)
            return Response(result)
        return Response(serializer.errors)


