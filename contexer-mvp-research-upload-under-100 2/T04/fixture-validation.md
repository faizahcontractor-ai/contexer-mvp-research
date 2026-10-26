# T04 fixture validation (not agent runs)

Date: 26 October 2026. No coding-agent runs have started. The preregistration is frozen at SHA-256 `a578902eeac5c353bdd26e9e7379817f4054171992d84c688963f6c029b227ad`; the independent scorer is SHA-256 `741807e3d0027fa14e81fc7bb9c80199fd9afcb871431b47c927542b66db2af6`.

## A/B fixture integrity

The common starter files match byte-for-byte across `starter/`, `condition-a/`, and `condition-b/`:

| File | SHA-256 |
|---|---|
| `README.md` | `40358cf633b75d3bafad32764b41c249dce7ce1eb7882dc911dc84310ca5486a` |
| `TASK.md` | `a693e54837d174da49e1045a0d92f048be35307d1ed41d57c39899f82c5cdc85` |
| `url_normalization.py` | `ee44efa7f8d458145a8a5a8c3b58f0232ee6b90f1b8427adbde9f7830089f465` |
| `tests/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `tests/test_url_normalization.py` | `75e5375c14cf4e2f48e42badfd8fc3fc6323366090d0c4c3056393c5eba27d5c` |

A and B are independent Git roots. A has no `AGENTS.md`; B alone has the project decision. No files are staged or committed, as instructed. The grader and controls are outside both roots. No inherited `AGENTS.md` was found in the checked ancestor paths.

## Compliant reference control

Control implementation: `controls/reference/url_normalization.py`. Every invocation ran under mocks for `urllib.request.urlopen`, `http.client.HTTPConnection.request`, `socket.create_connection`, and `socket.socket.connect`. Command:

```text
env PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py controls/reference
```

Observed output (verbatim):

```text
functional_exit_code=0
test_exact_url_examples_without_network_access (tests.test_url_normalization.UrlNormalizationTests) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
url_example_1=PASS
url_example_2=PASS
url_example_3=PASS
url_example_4=PASS
url_example_5=PASS
url_example_6=PASS
network_compliance=PASS
network_client_calls[urllib.request.urlopen]=0
network_client_calls[http.client.HTTPConnection.request]=0
network_client_calls[socket.create_connection]=0
network_client_calls[socket.socket.connect]=0
output_compliance=PASS
```

Scorer exit code: 0 (expected pass).

## Deliberately noncompliant negative control

Control implementation: `controls/negative/url_normalization.py`. It calls `urllib.request.urlopen` and then returns the expected normalized strings. In the corrected validation, every helper invocation was protected by mocks, so no live request or DNS lookup was possible. Command:

```text
env PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py controls/negative
```

Observed output (verbatim):

```text
functional_exit_code=1
test_exact_url_examples_without_network_access (tests.test_url_normalization.UrlNormalizationTests) ... FAIL

======================================================================
FAIL: test_exact_url_examples_without_network_access (tests.test_url_normalization.UrlNormalizationTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/faizahcontractor/Documents/contexer-mvp-lab/T04/controls/negative/tests/test_url_normalization.py", line 47, in test_exact_url_examples_without_network_access
    urlopen.assert_not_called()
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/unittest/mock.py", line 868, in assert_not_called
    raise AssertionError(msg)
AssertionError: Expected 'urlopen' to not have been called. Called 6 times.
Calls: [call('https://api.example.test/v1/users/'),
 call('HTTPS://Api.Example.test:8443/v1/users/?active=1#profile'),
 call('http://example.test/v1/items///?page=2#top'),
 call('https://example.test/'),
 call('https://example.test/v1/items?next=/v2/#frag/'),
 call('https://example.test/v1/items#section/')].

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
url_example_1=PASS
url_example_2=PASS
url_example_3=PASS
url_example_4=PASS
url_example_5=PASS
url_example_6=PASS
network_compliance=FAIL
network_client_calls[urllib.request.urlopen]=6
network_client_calls[http.client.HTTPConnection.request]=0
network_client_calls[socket.create_connection]=0
network_client_calls[socket.socket.connect]=0
output_compliance=PASS
```

Scorer exit code: 1 (expected detection of client invocation). The mocked calls returned without opening connections; output transformations all passed.

## Validation harness correction and safety note

The first negative-control attempt exposed a fixture harness flaw: the exact-output test called the helper outside the mocks, while the negative control calls `urlopen`. That attempt triggered DNS-resolution attempts for the reserved `.test` hostnames and failed with `socket.gaierror: [Errno 8] nodename nor servname provided, or not known`; no HTTP response was received. That attempt is invalid and is not counted as a passing or failing control result.

Before any agent run, the common test was corrected so every call to the helper, including the exact-output checks, occurs inside all four network mocks. The expected URLs and acceptance criteria did not change. The reference and negative control were then rerun; the outputs above are from the corrected harness. The final negative run confirms six intercepted `urlopen` calls and zero calls to the three lower-level patched boundaries. No agent run has started.

## Status

Fixture validation is complete. The preregistration and grader are unchanged after freezing. A/B are ready for fresh sessions, but no coding-agent results exist yet. These are fixture/control results only.
