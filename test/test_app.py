import json
import pytest

from src.app import sum_rng

test_total_sample_data = [10]
test_total_data = [({"total": 50000005000000})]


def test_total_invalid_url(app, client):
    result = client.get('/')
    assert result.status_code == 404


@pytest.mark.parametrize("expected", test_total_sample_data)
def test_sum_range(expected):
    numbers_to_add = list(range(5))
    actual_output = sum_rng(numbers_to_add[0], numbers_to_add[-1])
    assert actual_output == expected


@pytest.mark.parametrize("expected", test_total_data)
def test_total(app, client, expected):
    result = client.get('/total')
    assert result.status_code == 200
    assert expected == json.loads(result.get_data(as_text=True))
