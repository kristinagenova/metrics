import pytest


@pytest.fixture
def missing_show_field_fixture():
    return {
                "filter": {
                    "country": "CA"
                },
                "group": ["channel"],
                "sort": {
                    "order": "-",
                    "field": "CPI"
                }
            }

@pytest.fixture
def missing_filter_field_fixture():
    return {
                "show": ["CPI"],
                "group": ["channel"],
                "sort": {
                    "order": "-",
                    "field": "CPI"
                }
            }

@pytest.fixture
def missing_group_field_fixture():
    return {
                "show": ["CPI"],
                "filter": {
                    "country": "CA"
                },
                "sort": {
                    "order": "-",
                    "field": "CPI"
                }
            }

@pytest.fixture
def missing_sort_field_fixture():
    return {
                "show": ["CPI"],
                "filter": {
                    "country": "CA"
                },
                "group": ["channel"]
            }

@pytest.fixture
def missing_filter_values_fixture():
    return {
            "show": ["CPI"],
            "filter": {
            },
            "group" : ["channel"],
            "sort" : {
                "order" : "-",
                "field" : "CPI"
            }
        }

@pytest.fixture
def wrong_filter_values_fixture():
    return {
            "show": ["CPI"],
            "filter": {
                "country": "Foo"
            },
            "group": ["channel"],
            "sort": {
                "order": "-",
                "field": "CPI"
            }
        }