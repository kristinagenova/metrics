from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class DateSerializer(serializers.Serializer):
    approx = serializers.CharField(max_length=4, allow_blank=True)
    date = serializers.DateField()

    def validate(self, attrs):
        if attrs['approx'] not in ["to", "from", ""]:
            raise ValidationError("The only accepted keywords here are the following: from, to or leave blank")
        return attrs


class FilterSerializer(serializers.Serializer):
    date = DateSerializer(required=False)
    channel = serializers.CharField(max_length=20, required=False, allow_blank=False)
    country = serializers.CharField(max_length=2, required=False, allow_blank=False)
    os = serializers.CharField(max_length=20, required=False, allow_blank=False)

    def validate(self, attrs):
        if len(attrs) == 0:
            raise ValidationError("There must be at least one filter. Possible filters are: date, channel, country, os")
        return attrs


class SortSerializer(serializers.Serializer):
    order = serializers.CharField(max_length=1, allow_blank=True)
    field = serializers.CharField(max_length=10)

    def validate(self, attrs):
        if attrs['order'] not in ["-", ""]:
            raise ValidationError("For DESC order use '-', for ASC leave blank. Nothing else is allowed")
        if attrs['field'] not in ["impressions", "clicks", "installs", "spend", "revenue", "CPI", "channel", "country", "os"]:
            raise ValidationError("The only accepted key words here are the following: impressions, clicks, installs,"
                                  " spend, revenue, CPI, channel, country, os")
        return attrs


class GroupListSerializer(serializers.ListSerializer):
    child = serializers.CharField(max_length=20, allow_blank=False)

    def validate(self, attrs):
        for attr in attrs:
            if attr not in ["date", "channel", "country", "os"]:
                raise ValidationError("Only the accepted key words here are the following:"
                                      "date, channel, country, os ")
        return attrs


class ShowListSerializer(serializers.ListSerializer):
    child = serializers.CharField(max_length=20, allow_blank=False)

    def validate(self, attrs):
        for attr in attrs:
            if attr not in ["impressions", "clicks", "installs", "spend", "CPI", "revenue"]:
                raise ValidationError("Only the accepted key words here are the following: "
                                      "impressions, clicks, installs, spend, revenue, CPI")
        return attrs


class MetricsSerializer(serializers.Serializer):
    show = ShowListSerializer(allow_empty=False)
    filter = FilterSerializer(required=True)
    group = GroupListSerializer(allow_empty=False)
    sort = SortSerializer(required=True)