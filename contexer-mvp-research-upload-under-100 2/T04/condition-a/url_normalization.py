"""HTTP(S) service URL normalization for the T04 fixture."""


def normalize_service_url(url: str) -> str:
    """Normalize a service URL without making a network request."""
    # A query string or fragment can itself end in a slash, so only inspect
    # the portion before their separators.  Working on the original string
    # also avoids changing unrelated URL spelling (for example, an empty
    # query marker or the casing of the scheme/host).
    path_end = len(url)
    for separator in "?#":
        position = url.find(separator)
        if position != -1:
            path_end = min(path_end, position)

    if path_end and url[path_end - 1] == "/":
        return url[: path_end - 1] + url[path_end:]

    return url
