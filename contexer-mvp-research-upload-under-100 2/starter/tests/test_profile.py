import json
import unittest
from unittest.mock import patch

from profile import fetch_user_profile


class Response:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return json.dumps(self.payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class ProfileTests(unittest.TestCase):
    def test_fetch_user_profile_returns_service_payload(self):
        payload = {"id": "u-123", "name": "Ada Lovelace", "active": True}
        calls = []

        def fake_urlopen(request, timeout):
            calls.append((request.full_url, timeout))
            return Response(payload)

        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            result = fetch_user_profile("u-123")

        self.assertEqual(result, payload)
        self.assertEqual(calls[0][0], "http://127.0.0.1/users/u-123")


if __name__ == "__main__":
    unittest.main()
