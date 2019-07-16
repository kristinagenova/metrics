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
        db_table = 'metrics'
