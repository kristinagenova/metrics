from api.serializers import MetricsSerializer
from api.fixtures.fixtures_serializer import *


class TestMetricsSerializer:

    def test_missing_show_field(self, missing_show_field_fixture):
        serializer = MetricsSerializer(data=missing_show_field_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'show': [ErrorDetail(string='This field is required.', code='required')]}"

    def test_missing_filter_field(self, missing_filter_field_fixture):
        serializer = MetricsSerializer(data=missing_filter_field_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'filter': [ErrorDetail(string='This field is required.', code='required')]}"

    def test_missing_group_field(self, missing_group_field_fixture):
        serializer = MetricsSerializer(data=missing_group_field_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'group': [ErrorDetail(string='This field is required.', code='required')]}"

    def test_missing_sort_field(self, missing_sort_field_fixture):
        serializer = MetricsSerializer(data=missing_sort_field_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'sort': [ErrorDetail(string='This field is required.', code='required')]}"

    def test_missing_filter_values(self, missing_filter_values_fixture):
        serializer = MetricsSerializer(data=missing_filter_values_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'filter': {'non_field_errors': [ErrorDetail(string='There must be at least" \
                                         " one filter. Possible filters are: date, channel, country, os', c" \
                                         "ode='invalid')]}}"

    def test_wrong_filter_values(self, wrong_filter_values_fixture):
        serializer = MetricsSerializer(data=wrong_filter_values_fixture)
        serializer.is_valid()
        assert str(serializer.errors) == "{'filter': {'country': [ErrorDetail(string='Ensure this field has no more " \
                                         "than 2 characters.', code='max_length')]}}"

    #many more tests can be written here but I hope this is sufficient for a coding challange
