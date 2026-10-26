# Project instructions

For valid absolute HTTP(S) URLs, `normalize_service_url(url: str) -> str` must make no network calls and must only remove exactly one final `/` from the URL path when present. Preserve the scheme and authority exactly, preserve the rest of the path exactly, and leave query and fragment untouched. Do not normalize or trim any other part of the URL. A root path `/` becomes an empty path; multiple trailing path slashes lose only the final one.
