import http.client
import socket
import unittest
import urllib.request
from unittest.mock import patch

from url_normalization import normalize_service_url


EXAMPLES = (
    (
        "https://api.example.test/v1/users/",
        "https://api.example.test/v1/users",
    ),
    (
        "HTTPS://Api.Example.test:8443/v1/users/?active=1#profile",
        "HTTPS://Api.Example.test:8443/v1/users?active=1#profile",
    ),
    (
        "http://example.test/v1/items///?page=2#top",
        "http://example.test/v1/items//?page=2#top",
    ),
    ("https://example.test/", "https://example.test"),
    (
        "https://example.test/v1/items?next=/v2/#frag/",
        "https://example.test/v1/items?next=/v2/#frag/",
    ),
    (
        "https://example.test/v1/items#section/",
        "https://example.test/v1/items#section/",
    ),
    # Keep delimiters present even when their query or fragment is empty.
    ("HTTPS://User:Pass@Api.Example.test:8443/v1/?", "HTTPS://User:Pass@Api.Example.test:8443/v1?"),
    ("https://example.test/v1/#", "https://example.test/v1#"),
)


class UrlNormalizationTests(unittest.TestCase):
    def test_exact_url_examples_without_network_access(self):
        # Keep every helper invocation under network mocks, including in the
        # negative-control suite, so validation cannot perform live I/O.
        with patch("urllib.request.urlopen") as urlopen, \
             patch("http.client.HTTPConnection.request") as http_request, \
             patch("socket.create_connection") as create_connection, \
             patch("socket.socket.connect") as socket_connect:
            for source, expected in EXAMPLES:
                with self.subTest(source=source):
                    self.assertEqual(normalize_service_url(source), expected)

        urlopen.assert_not_called()
        http_request.assert_not_called()
        create_connection.assert_not_called()
        socket_connect.assert_not_called()


if __name__ == "__main__":
    unittest.main()
