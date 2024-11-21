import requests
from typing import Optional, Dict, Any


def make_mattermost_api_call(
    mattermost_url: str,
    api_token: str,
    endpoint: str,
    method: str = "GET",
    port: int = 8065,
    json_body: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Makes an API call to a Mattermost server and returns the response as a dictionary.

    Args:
        mattermost_url (str): The base URL of the Mattermost server (e.g., 'https://example.com').
        api_token (str): The personal access token for authentication.
        endpoint (str): The API endpoint (e.g., '/api/v4/users/me').
        method (str): The HTTP method to use ('GET', 'POST', 'PATCH', 'DELETE', etc.).
        port (int): The port on which Mattermost is running. Default is 8065.
        json_body (Optional[Dict[str, Any]]): The JSON body for the request (default is None).
        params (Optional[Dict[str, str]]): Query parameters for the request (default is None).

    Returns:
        Dict[str, Any]: The JSON response as a dictionary.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
    """
    url = f"{mattermost_url}:{port}{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=json_body,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to make API call to {url}: {e}")
