from api.services import MetricsService
from api.fixtures.fixtures_service import *


class TestConvertFilterValues:

    def test_with_country_and_date(self, filter_with_country_and_date):
        service = MetricsService()
        filters = service.convert_filter_values(data=filter_with_country_and_date)

        assert filters["filter"] == {'country': 'CA', 'date': '2017-05-17'}

    #could have more tests here

class TestConvertSortValues:

    def test_with_show_with_cpi(self, filter_with_show_with_cpi):
        service = MetricsService()
        show = service.convert_show_values(data=filter_with_show_with_cpi)

        assert str(show['CPI']) == "Sum(F(spend)) / Sum(F(installs))"

    #could have more tests here
