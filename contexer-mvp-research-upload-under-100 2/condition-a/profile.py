"""Profile service functions for the T01 fixture."""

from urllib.parse import quote

from shared_client import client


def fetch_user_profile(user_id: str) -> dict:
    """Fetch and return one user's profile from the service."""
    return client.get_json(f"/users/{quote(user_id, safe='')}")
