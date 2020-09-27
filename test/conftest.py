import pytest

from src.app import app as sum_app


@pytest.fixture
def app():
    yield sum_app


@pytest.fixture
def client(app):
    return app.test_client()