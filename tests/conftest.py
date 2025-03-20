import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_currency_data():
    """Mock currency data response for testing."""
    return {
        "date": "2023-03-20",
        "aud": {
            "usd": 0.6712,
            "eur": 0.6152,
            "gbp": 0.5232,
            "jpy": 101.32,
            "cad": 0.9123
        }
    }

@pytest.fixture
def mock_get_currency_data():
    """Patch the get_currency_data function to avoid actual API calls during tests."""
    with patch("simple_currency_converter.core.get_currency_data") as mock:
        yield mock

@pytest.fixture
def mock_requests_get():
    """Mock requests.get to avoid actual API calls during tests."""
    with patch("requests.get") as mock:
        mock_response = MagicMock()
        mock.return_value = mock_response
        yield mock, mock_response 