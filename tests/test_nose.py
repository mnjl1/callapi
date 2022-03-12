from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none, assert_list_equal, assert_is_none

from apicall import parse_json


@patch("apicall.requests.get")
def test_parse_json_response_ok(mock_get):
    users = [{"id": 1, "username": "Elton"}]
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = users

    response = parse_json()

    assert_is_not_none(response)
    assert_list_equal(response.json(), users)


@patch("apicall.requests.get")
def test_parse_json_response_is_not_ok(mock_get):
    mock_get.return_value = Mock(ok=False)

    response = parse_json()

    assert_is_none(response)


@patch("apicall.requests.get")
def test_getting_name_from_json(mock_get_todos):
    users = {"id": 1, "username": "Elton"}

    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [users]

    response = parse_json()

    assert (response.json()[0]["username"], "Elton")
