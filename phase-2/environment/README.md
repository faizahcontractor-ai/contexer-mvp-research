# Environment and reproduction

The saved Python environment uses Python 3.9.6, pandas 2.2.3, and scikit-learn 1.6.1 for the synthetic classifier. The full original pinned files are copied here as requirements.txt and requirements-lock.txt.

From the onboarding-contexer directory, create a virtual environment and install the direct requirements:

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r phase-2/environment/requirements.txt

Then run the classifier with .venv/bin/python phase-2/dataset/sample_analysis.py. Compare its stdout with phase-2/dataset/sample-output.txt. The historical full environment lock is supplied for inspection; recreating that entire Jupyter environment is not required for the classifier.

The agent-run evidence is historical. Reproducing an agent run requires the corresponding coding-agent account, model access, and fresh sessions; no credentials or local runtime state are included. The frozen scorers are in the existing public pilot bundle linked from the Phase 2 README. T04 scoring only invokes the helper inside the preregistered monkeypatches; never make a live network request.
