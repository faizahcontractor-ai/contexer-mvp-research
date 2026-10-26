"""Synthetic authenticated HTTP client with bounded retry behavior.

This fixture only talks to its local test server when tests run.
"""

from __future__ import annotations

import json
import time
from urllib.error import HTTPError, URLError
import urllib.request


class SharedClient:
    def __init__(self, base_url: str = "http://127.0.0.1", token: str = "fixture-token", retries: int = 1):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.retries = retries

    def get_json(self, path: str):
        """GET a JSON resource with fixture auth and one bounded retry by default."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        request = urllib.request.Request(url, headers={"Authorization": f"Bearer {self.token}"})
        for attempt in range(self.retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=2) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (HTTPError, URLError):
                if attempt >= self.retries:
                    raise
                time.sleep(0.01)


client = SharedClient()
