from django.db.models import Sum, FloatField
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Metrics
from api.serializers import MetricsSerializer


class MetricsView(viewsets.ViewSet):

    @action(detail=True, methods=['post'])
    def get_metrics_controller(self, request):
        serializer = MetricsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            group_by = data['group']
            show = self.get_show_values(data.get('show'))
            sort = '{0}{1}'.format(data['sort']['order'], data['sort']['field'])
            filters = self.get_filter_values(data['filter'])

            result = self.get_metrics(group_by=group_by, show=show, filters=filters, sort=sort)
            return Response(result)
        return Response(serializer.errors)

    def get_filter_values(self, data):
        result = {}
        for filter_field in data:
            if filter_field is not "date":
                result['{0}'.format(filter_field)] = data[filter_field]
            if filter_field is "date":
                if data[filter_field]['approx'] == 'to':
                    result['{0}__{1}'.format('date', 'lte')] = data[filter_field]['date']
                elif data[filter_field]['approx'] == "from":
                    result['{0}__{1}'.format('date', 'gte')] = data[filter_field]['date']
                elif data[filter_field]['approx'] == "":
                    result['{0}'.format('date')] = data[filter_field]['date']
        return result

    def get_show_values(self, data):
        result = {}
        for field_to_be_shown in data:
            if field_to_be_shown == "CPI":
                result['{0}'.format(field_to_be_shown)] = \
                    Sum('spend', output_field=FloatField()) / Sum('installs', output_field=FloatField())
            else:
                result['{0}'.format(field_to_be_shown)] = Sum(field_to_be_shown)
        return result

    def get_metrics(self, group_by, show, filters, sort):
        result = Metrics.objects \
            .values(*group_by) \
            .annotate(**show) \
            .filter(**filters)\
            .order_by(sort)
        return result
