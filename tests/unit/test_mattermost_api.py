import unittest
import requests
from mattermost_api.mattermost_api import make_mattermost_api_call
from unittest.mock import patch


class TestMattermostAPICall(unittest.TestCase):
    @patch("mattermost_api.mattermost_api.requests.request")
    def test_get_request_success(self, mock_request):
        # Mock response
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"key": "value"}

        # Call the function
        response = make_mattermost_api_call(
            mattermost_url="https://example.com",
            api_token="fake_token",
            endpoint="/api/v4/users/me",
            method="GET"
        )

        # Assertions
        self.assertEqual(response, {"key": "value"})
        mock_request.assert_called_once_with(
            method="GET",
            url="https://example.com:8065/api/v4/users/me",
            headers={
                "Authorization": "Bearer fake_token",
                "Content-Type": "application/json",
            },
            json=None,
            params=None,
            timeout=10
        )

    @patch("mattermost_api.mattermost_api.requests.request")
    def test_post_request_with_body(self, mock_request):
        # Mock response
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {"success": True}

        # Call the function with a JSON body
        response = make_mattermost_api_call(
            mattermost_url="https://example.com",
            api_token="fake_token",
            endpoint="/api/v4/posts",
            method="POST",
            json_body={"content": "Hello World"}
        )

        # Assertions
        self.assertEqual(response, {"success": True})
        mock_request.assert_called_once_with(
            method="POST",
            url="https://example.com:8065/api/v4/posts",
            headers={
                "Authorization": "Bearer fake_token",
                "Content-Type": "application/json",
            },
            json={"content": "Hello World"},
            params=None,
            timeout=10
        )

    @patch("mattermost_api.mattermost_api.requests.request")
    def test_request_failure(self, mock_request):
        # Mock a failure response
        mock_request.return_value.status_code = 404
        mock_request.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Client Error: Not Found")

        # Call the function and expect a RuntimeError
        with self.assertRaises(RuntimeError) as context:
            make_mattermost_api_call(
                mattermost_url="https://example.com",
                api_token="fake_token",
                endpoint="/api/v4/unknown",
                method="GET"
            )

        # Check the exception message
        self.assertIn("Failed to make API call to", str(context.exception))


if __name__ == "__main__":
    unittest.main()
