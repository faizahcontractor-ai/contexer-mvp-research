# Synthetic profile service fixture

Small, dependency-free Python fixture for T01. `shared_client.py` is the existing service client; it provides bearer authentication and bounded retries. Tests replace the transport with an in-memory fake, so running them does not contact a network.

Run the checks with `python3 -m unittest discover -v`.
