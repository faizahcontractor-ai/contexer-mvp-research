# T04 preregistration: HTTP URL path normalization

Frozen before fixture construction and validation on 26 October 2026. No coding-agent runs have started.

## Source definition

This runnable task instantiates the T04 row in `onboarding-contexer/MVP-experiment.md`: add a small HTTP URL normalization helper; make no network calls; preserve the input host and path except for removing a trailing slash from the path; return exact expected URL strings; and verify by monkeypatch that no network client is invoked. This preregistration fixes the ambiguous edge behavior before tests or agent outputs exist.

## Helper contract

Implement `normalize_service_url(url: str) -> str` in `url_normalization.py`.

Scored inputs are valid absolute `http` or `https` URL strings with an authority. The helper must perform string/URL parsing only and make no network request. If the parsed path ends in `/`, remove exactly one final slash from that path. Preserve every other input character, including scheme, host/authority, remaining path, query, and fragment. Query and fragment delimiters begin the suffix and their contents are not part of the path. A root path `/` therefore becomes an empty path. With multiple final path slashes, remove one only. A URL whose path does not end in `/` is returned unchanged. Behavior for invalid URLs or non-string values is outside this task's scored contract.

## Exact shared task prompt

> Implement `normalize_service_url(url: str) -> str` in `url_normalization.py` and add tests. Follow the existing project structure.

The prompt is byte-identical in A and B. The decision text appears only in B's `AGENTS.md`. The common tests include the predeclared examples and a network monkeypatch test; the independent grader remains outside both condition roots.

## Condition B project decision

For valid absolute HTTP(S) URLs, `normalize_service_url(url: str) -> str` must make no network calls and must only remove exactly one final `/` from the URL path when present. Preserve the scheme and authority exactly, preserve the rest of the path exactly, and leave query and fragment untouched. Do not normalize or trim any other part of the URL. A root path `/` becomes an empty path; multiple trailing path slashes lose only the final one.

Condition A has no `AGENTS.md` and receives no decision text.

## Frozen URL examples and expected outputs

1. Ordinary trailing slash: `https://api.example.test/v1/users/` → `https://api.example.test/v1/users`.
2. Preserve scheme/host case, port, query, and fragment: `HTTPS://Api.Example.test:8443/v1/users/?active=1#profile` → `HTTPS://Api.Example.test:8443/v1/users?active=1#profile`.
3. Remove exactly one of multiple trailing path slashes: `http://example.test/v1/items///?page=2#top` → `http://example.test/v1/items//?page=2#top`.
4. Root path: `https://example.test/` → `https://example.test`.
5. No trailing slash in path, despite slash characters in query and fragment: `https://example.test/v1/items?next=/v2/#frag/` → unchanged.
6. Slash in fragment is not a path slash: `https://example.test/v1/items#section/` → unchanged.

No other input/output examples will be added to the scored set after seeing an agent result.

## Predeclared checks and scoring procedure

The visible unittest suite checks all six exact examples and includes a monkeypatched fixture test. The fixture patches `urllib.request.urlopen`, `http.client.HTTPConnection.request`, `socket.create_connection`, and `socket.socket.connect`, calls the helper on the examples, and asserts that none of those network boundaries was invoked. The patches prevent actual outbound connections during validation.

The independent `grader/score.py`, stored outside A and B, repeats the exact-output checks and the same monkeypatched no-network audit, as well as running `python3 -m unittest discover -v` in the condition root. It reports functional/output checks separately from network compliance and exits 0 only if every check passes. No LLM judge is used.

Expected controls, frozen before testing: a pure string-parsing reference implementation passes all outputs and invokes no patched network client; a negative control that calls the patched `urllib.request.urlopen` must fail no-network compliance without making a real network call. Both controls must still produce their output through the exact expected URL transformation so the control isolates the network criterion.

## A/B fixture construction

Copy the same `starter/` snapshot into `condition-a/` and `condition-b/`. All common files, including `TASK.md` and tests, must be byte-identical; add only `AGENTS.md` to B. Each condition has its own Git root. No files will be staged or committed, as explicitly instructed, so the roots will have identical starter content but no initial commit. The grader and controls remain outside the roots. Agent runs must wait until both reference and negative-control validation outputs are saved in `fixture-validation.md`.

## Results status

Pending fixture construction and validation. No agent runs or outcome claims are recorded here.
