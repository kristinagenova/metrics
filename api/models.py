from django.db import models


class Metrics(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    channel = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=20)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    class Meta:
        db_table = "metrics"

    def get_metrics_from_db(self, group_by, show, filters, sort):
        return Metrics.objects \
            .values(*group_by) \
            .annotate(**show) \
            .filter(**filters)\
            .order_by(sort)
