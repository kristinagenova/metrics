from django.db.models import Sum, F

from api.models import Metrics
from api.fixtures.fixtures_model import *

class TestMetricsGet:

    @pytest.mark.django_db
    def test_group_by(db, django_db_setup):
        metrics_model = Metrics()
        result = metrics_model.get_metrics_from_db(group_by=["channel", "country"],
                                                   show={"impressions": Sum(F("impressions")), "clicks": Sum(F("clicks"))},
                                                   filters={"date": "2017-05-17"},
                                                   sort="-clicks")
        assert result.count() == 4
        assert result[0]['channel'] == "facebook"
        assert result[0]['country'] == "CA"
        assert result[3]['channel'] == "google"
        assert result[3]['country'] == "US"

    @pytest.mark.django_db
    def test_show(db, django_db_setup):
        metrics_model = Metrics()
        result = metrics_model.get_metrics_from_db(group_by=["channel", "country"],
                                                   show={"impressions": Sum(F("impressions")), "clicks": Sum(F("clicks"))},
                                                   filters={"country": "CA"},
                                                   sort="-clicks")
        assert result.count() == 2
        assert result[0]['impressions'] == 15
        assert result[0]['clicks'] == 6
        assert result[1]['impressions'] == 10
        assert result[1]['clicks'] == 4

    @pytest.mark.django_db
    def test_filter(db, django_db_setup):
        metrics_model = Metrics()
        result = metrics_model.get_metrics_from_db(group_by=["channel", "country"],
                                                   show={"impressions": Sum(F("impressions")), "clicks": Sum(F("clicks"))},
                                                   filters={"country": "CA"},
                                                   sort="-clicks")
        assert result.count() == 2
        assert result[0]['country'] == "CA"
        assert result[1]['country'] == "CA"

    @pytest.mark.django_db
    def test_sort_desc(db, django_db_setup):
        metrics_model = Metrics()
        result = metrics_model.get_metrics_from_db(group_by=["channel", "country"],
                                                   show={"impressions": Sum(F("impressions")), "clicks": Sum(F("clicks"))},
                                                   filters={"date": "2017-05-17"},
                                                   sort="-clicks")
        assert result.count() == 4
        assert result[0]['clicks'] >= result[1]['clicks']
        assert result[1]['clicks'] >= result[2]['clicks']

    @pytest.mark.django_db
    def test_sort_asc(db, django_db_setup):
        metrics_model = Metrics()
        result = metrics_model.get_metrics_from_db(group_by=["channel", "country"],
                                                   show={"impressions": Sum(F("impressions")), "clicks": Sum(F("clicks"))},
                                                   filters={"date": "2017-05-17"},
                                                   sort="clicks")
        assert result.count() == 4
        assert result[2]['clicks'] >= result[1]['clicks']
        assert result[1]['clicks'] >= result[0]['clicks']

