from unittest.mock import MagicMock, patch
import pytest
import requests
import os


def fetch_data():
    url = f"https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/latest/USD"
    response = requests.get(url)
    return response.json()

@pytest.fixture
def mock_response():
    mock_response = MagicMock(spec=requests.Response)
    mock_response.json.return_value = {'result': 'error', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms-of-use': 'https://www.exchangerate-api.com/terms', 'error-type': 'invalid-key'}
    return mock_response

@patch('requests.get')
def test_fetch_data(mock_get, mock_response):
    """Тестирует функцию fetch_data с мокированием."""
    mock_get.return_value = mock_response
    data = fetch_data()
    assert data == {'result': 'error', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms-of-use': 'https://www.exchangerate-api.com/terms', 'error-type': 'invalid-key'}
    mock_get.assert_called_once()
    mock_response.json.assert_called_once()

