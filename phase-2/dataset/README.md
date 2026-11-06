# Synthetic classifier dataset example

sample_analysis.py creates a deterministic 200-row binary classification dataset in memory (random_state=42), uses a stratified 75/25 train/test split, and fits logistic regression. No private or downloaded dataset is used. The saved output reports 47/50 correct test predictions (0.940 accuracy) and confusion matrix [[24, 1], [2, 23]].

Run from onboarding-contexer/ with the pinned environment:

    .venv/bin/python phase-2/dataset/sample_analysis.py

The classifier is a reproducibility smoke test for the original onboarding work. It is not an agent benchmark and does not measure Contexer.
