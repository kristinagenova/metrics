from django.db.models import Sum, FloatField


class MetricsService:

    def convert_filter_values(self, data):
        result = {}
        for filter_field in data:
            if filter_field is not "date":
                result[filter_field] = data[filter_field]
            if filter_field is "date":
                if data[filter_field]['approx'] == 'to':
                    result["date__lte"] = data[filter_field]['date']
                elif data[filter_field]['approx'] == "from":
                    result["date__lte"] = data[filter_field]['date']
                elif data[filter_field]['approx'] == "":
                    result["date"] = data[filter_field]['date']
        return result

    def convert_show_values(self, data):
        result = {}
        for field_to_be_shown in data:
            if field_to_be_shown == "CPI":
                result[field_to_be_shown] = \
                    Sum("spend", output_field=FloatField()) / Sum("installs", output_field=FloatField())
            else:
                result[field_to_be_shown] = Sum(field_to_be_shown)
        return result
