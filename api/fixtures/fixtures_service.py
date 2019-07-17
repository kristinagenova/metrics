import pytest


@pytest.fixture
def filter_with_country_and_date():
    return {
            "filter": {
                "country": "CA",
                "date": "2017-05-17"
            },
        }

@pytest.fixture
def filter_with_show_with_cpi():
    return ["CPI"]
