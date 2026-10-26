"""HTTP(S) service URL normalization for the T04 fixture."""

from urllib.parse import urlsplit


def normalize_service_url(url: str) -> str:
    """Remove one trailing slash from the path of an absolute HTTP(S) URL.

    The original string is edited in place rather than reconstructed from
    parsed components, so its scheme, authority, query, and fragment retain
    their exact spelling.
    """
    parsed = urlsplit(url)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return url

    # Query and fragment delimit the path.  Locate the end in the original
    # string so removing a slash cannot alter any other URL component.
    path_end = len(url)
    for delimiter in ("?", "#"):
        delimiter_index = url.find(delimiter)
        if delimiter_index != -1:
            path_end = min(path_end, delimiter_index)

    if path_end > 0 and url[path_end - 1] == "/":
        return url[: path_end - 1] + url[path_end:]
    return url
