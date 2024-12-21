import requests
import random
from typing import Optional

class HTTPClient:
    """
    A versatile HTTP client for making requests with user-agent rotation.

    Args:
        user_agents: A list of user-agent strings to rotate.
    """

    def __init__(self, user_agents: Optional[list[str]] = None):
        self.user_agents = user_agents or [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/117.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/605.1.15",
        ]

    def get(self, url: str, headers: Optional[dict] = None) -> requests.Response:
        """
        Sends a GET request to the specified URL.

        Args:
            url: The URL to send the request to.
            headers: Optional headers to include in the request.

        Returns:
            The response object.
        """

        headers = headers or {}
        headers['User-Agent'] = random.choice(self.user_agents)

        response = requests.get(url, headers=headers)
        return response

    def post(self, url: str, data: dict, headers: Optional[dict] = None) -> requests.Response:
        """
        Sends a POST request to the specified URL.

        Args:
            url: The URL to send the request to.
            data: The data to send in the request body.
            headers: Optional headers to include in the request.

        Returns:
            The response object.
        """

        headers = headers or {}
        headers['User-Agent'] = random.choice(self.user_agents)

        response = requests.post(url, data=data, headers=headers)
        return response