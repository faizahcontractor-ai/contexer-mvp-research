"""Independent deterministic T04 functional/output/network scorer."""
from __future__ import annotations

import importlib
import http.client
import subprocess
import sys
import socket
import urllib.request
from pathlib import Path
from unittest.mock import patch

EXAMPLES = (
    ("https://api.example.test/v1/users/", "https://api.example.test/v1/users"),
    ("HTTPS://Api.Example.test:8443/v1/users/?active=1#profile", "HTTPS://Api.Example.test:8443/v1/users?active=1#profile"),
    ("http://example.test/v1/items///?page=2#top", "http://example.test/v1/items//?page=2#top"),
    ("https://example.test/", "https://example.test"),
    ("https://example.test/v1/items?next=/v2/#frag/", "https://example.test/v1/items?next=/v2/#frag/"),
    ("https://example.test/v1/items#section/", "https://example.test/v1/items#section/"),
)


def load_helper(root: Path):
    sys.path.insert(0, str(root))
    sys.modules.pop("url_normalization", None)
    return importlib.import_module("url_normalization")


def score(root: Path) -> int:
    functional = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-v"],
        cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    print(f"functional_exit_code={functional.returncode}")
    print(functional.stdout, end="")
    try:
        helper = load_helper(root)
    except Exception as exc:
        print(f"helper_import=FAIL ({type(exc).__name__}: {exc})")
        print("output_compliance=FAIL")
        print("network_compliance=FAIL")
        return 1

    outputs_ok = True
    with patch("urllib.request.urlopen") as urlopen, \
         patch("http.client.HTTPConnection.request") as http_request, \
         patch("socket.create_connection") as create_connection, \
         patch("socket.socket.connect") as socket_connect:
        for index, (source, expected) in enumerate(EXAMPLES, start=1):
            try:
                actual = helper.normalize_service_url(source)
                passed = actual == expected
                detail = "" if passed else f"expected {expected!r}, got {actual!r}"
            except Exception as exc:
                passed = False
                detail = f"unexpected {type(exc).__name__}: {exc}"
            outputs_ok = outputs_ok and passed
            print(f"url_example_{index}={'PASS' if passed else 'FAIL'}")
            if detail:
                print(f"url_example_{index}_detail={detail}")
        network_calls = {
            "urllib.request.urlopen": urlopen.call_count,
            "http.client.HTTPConnection.request": http_request.call_count,
            "socket.create_connection": create_connection.call_count,
            "socket.socket.connect": socket_connect.call_count,
        }
    network_ok = all(count == 0 for count in network_calls.values())
    print("network_compliance=" + ("PASS" if network_ok else "FAIL"))
    for name, count in network_calls.items():
        print(f"network_client_calls[{name}]={count}")
    print("output_compliance=" + ("PASS" if outputs_ok else "FAIL"))
    return 0 if functional.returncode == 0 and outputs_ok and network_ok else 1


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 grader/score.py CONDITION_DIRECTORY", file=sys.stderr)
        return 2
    return score(Path(sys.argv[1]).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
