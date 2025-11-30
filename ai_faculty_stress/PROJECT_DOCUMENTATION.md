# AI-Powered Faculty Stress Detector and Wellness Recommendation Expert System

Course: Artificial Intelligence and Machine Learning
Project Type: Hybrid AI System (Python + Visual Prolog)
Group Size: 2 Members

## 1. Project Overview

This project implements a hybrid intelligent system with two components:

- A Machine Learning (Python) module that predicts a faculty member's stress level (Low, Medium, High) from workload-related factors.
- A Rule-Based Expert System (Visual Prolog) that reads the predicted stress levels and outputs personalized wellness and workload recommendations.

The two components are integrated by writing and reading a simple Prolog facts file created by the Python module.

## 2. Learning Outcomes

The system demonstrates the ability to:

- Apply supervised machine learning techniques to a realistic, structured dataset.
- Convert numeric workload measures into a comprehensible stress label using a defined scoring system.
- Build a symbolic rule-based knowledge base for wellness recommendations.
- Integrate data-driven predictions with a rule-based expert system.

## 3. System Components and Files

Python side (directory: `ai_faculty_stress`):

- `generate_dataset.py` — generates a synthetic dataset (250 rows) conforming to the required schema and computes WSS and Stress_Level.
- `faculty_workload.csv` — generated dataset (columns: Faculty_ID, Subjects_Handled, Students_Total, Prep_Hours, Research_Load_Hours, Committee_Duties, Admin_Tasks, Meeting_Hours, Sleep_Hours, Weekend_Work, WSS, Stress_Level).
- `train_model.py` — trains a RandomForestClassifier on the generated dataset and saves the model to `stress_model.joblib`.
- `predict_and_export.py` — loads the trained model, predicts stress levels for entries in `faculty_workload.csv`, and writes three outputs:
  - `predicted_stress.txt` — simple text file `Faculty_ID StressLevel` per line.
  - `predicted_stress_facts.pl` — Prolog facts: `predicted_stress('F001','Medium').` for each faculty.
  - `recommender_example.pl` — a small SWI-Prolog example that consults the facts and prints recommendations.
- `requirements.txt` — Python package requirements.
- `README.md` — short run instructions.

Visual Prolog side:

- `visual_prolog_kb.txt` — Visual Prolog skeleton + instructions to create a Visual Prolog Console Application and integrate with `predicted_stress_facts.pl`.

Documentation:

- `PROJECT_DOCUMENTATION.md` — this file.

## 4. Dataset Specification

The dataset schema follows the specification provided:

Faculty_ID, Subjects_Handled, Students_Total, Prep_Hours, Research_Load_Hours, Committee_Duties, Admin_Tasks, Meeting_Hours, Sleep_Hours, Weekend_Work

The Python generator produces 250 rows with reasonable value distributions. Each row also includes computed WSS and Stress_Level according to the numeric rules below.

## 5. Workload Stress Score (WSS) — Numeric Basis

Point allocations (per variable):

- Subjects Handled: 1–2 = 1 pt, 3–4 = 2 pts, 5+ = 3 pts
- Total Students: <60 = 1 pt, 60–100 = 2 pts, >100 = 3 pts
- Preparation Hours: <6 = 1 pt, 6–10 = 2 pts, >10 = 3 pts
- Research Load: <4 = 1 pt, 4–6 = 2 pts, >6 = 3 pts
- Committee Duties: 0–1 = 1 pt, 2 = 2 pts, 3+ = 3 pts
- Administrative Tasks: 0–1 = 1 pt, 2–3 = 2 pts, 4+ = 3 pts
- Meeting Hours: <3 = 1 pt, 3–6 = 2 pts, >6 = 3 pts
- Sleep Hours: 7+ = 1 pt, 6 = 2 pts, <6 = 3 pts
- Weekend Work Frequency: 0 = 1 pt, 1–2 = 2 pts, 3+ = 3 pts

WSS = sum of all variable points. Minimum = 9, Maximum = 27.

Mapping WSS to Stress Level:

- 9–14: Low Stress
- 15–20: Medium Stress
- 21–27: High Stress

## 6. Integration Workflow (Required)

Execution order (must be followed):

1. Python ML Module
   - `generate_dataset.py` (optional if you already have a dataset) — creates `faculty_workload.csv` with WSS and Stress_Level.
   - `train_model.py` — trains model and saves `stress_model.joblib`.
   - `predict_and_export.py` — loads `stress_model.joblib`, predicts stress levels for rows in `faculty_workload.csv`, writes:
       - `predicted_stress.txt` (simple text)
       - `predicted_stress_facts.pl` (Prolog facts)
2. Visual Prolog Expert System
   - Load or include the facts from `predicted_stress_facts.pl`.
   - Apply the rule set to map stress levels to tailored recommendations.
   - Output recommendations per faculty member (console or file).

This ensures smooth communication: Python writes the facts, Visual Prolog reads them.

## 7. Visual Prolog Knowledge Base (design)

The Visual Prolog knowledge base must contain rules that map the stress level to recommendations. Example mappings:

- Low: Maintain current schedule; monitor workload.
- Medium: Prioritize tasks; delegate; ensure sufficient sleep.
- High: Reduce course load; request admin support; schedule regular breaks; seek wellness resources.

Implementation note: Visual Prolog syntax varies from SWI-Prolog. To simplify integration, the Python exporter writes standard Prolog facts which can be copied into a Visual Prolog predicate source file or parsed at runtime by a small input routine.

## 8. How to Run (short)

Requirements: Python 3.x, pip, and a Prolog environment (SWI-Prolog or Visual Prolog). For Visual Prolog development, use Visual Prolog IDE/version you have.

Commands (PowerShell):

```powershell
python -m pip install -r requirements.txt
python generate_dataset.py
python train_model.py
python predict_and_export.py
```

Then open the Prolog environment and load or consult the `predicted_stress_facts.pl` or load the facts into Visual Prolog source file per IDE instructions.

Example SWI-Prolog quick test (optional):

```powershell
swipl -q -f recommender_example.pl
```

## 9. Evaluation

On the synthetic dataset used for development, the RandomForest classifier reached approximately 86% test accuracy. With a real dataset, re-evaluate and tune the model.

## 10. Deliverables

- Python code implementing data generation, model training, and export (`generate_dataset.py`, `train_model.py`, `predict_and_export.py`)
- Trained model file: `stress_model.joblib` (generated after running training)
- Prolog facts file: `predicted_stress_facts.pl`
- Visual Prolog KB skeleton: `visual_prolog_kb.txt` (and instructions)
- Documentation: this `PROJECT_DOCUMENTATION.md` and `README.md`

## 11. Next steps and optional improvements

- Replace synthetic dataset with actual collected data (200–300 rows) and retrain the model.
- Expand the Visual Prolog rule base to use other numeric features (e.g., high WSS items) for more personalized recommendations.
- Add unit tests for WSS computation and the Python exporter.

---
If you'd like, I can now:

- Produce a Visual Prolog project ready for import (specify your Visual Prolog version), or
- Keep the Visual Prolog side minimal and provide a fully working SWI-Prolog example to demonstrate the integration.
