import unittest
from urllib.error import URLError

from shared_client import SharedClient


class Response:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class SharedClientTests(unittest.TestCase):
    def test_client_sends_bearer_token_and_retries_once(self):
        calls = []

        def transport(request, timeout):
            calls.append((request.full_url, request.get_header("Authorization"), timeout))
            if len(calls) == 1:
                raise URLError("synthetic transient failure")
            return Response(b'{"ok": true}')

        client = SharedClient(base_url="http://service.invalid", token="test-token", retries=1)
        # Replace the module-level URL opener used by the helper; no network is performed.
        import urllib.request
        original = urllib.request.urlopen
        urllib.request.urlopen = transport
        try:
            self.assertEqual(client.get_json("/health"), {"ok": True})
        finally:
            urllib.request.urlopen = original

        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][0], "http://service.invalid/health")
        self.assertEqual(calls[0][1], "Bearer test-token")
        self.assertEqual(calls[0][2], 2)


if __name__ == "__main__":
    unittest.main()
