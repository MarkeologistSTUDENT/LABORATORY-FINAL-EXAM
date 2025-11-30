AI-Powered Faculty Stress Detector

This small project generates a synthetic faculty workload dataset, computes a Workload Stress Score (WSS) per the provided rules, trains a RandomForest model to predict stress levels, and exports a simple text file usable by a Visual Prolog expert system.

Files
- `generate_dataset.py` - generates `faculty_workload.csv` with 250 rows and WSS/Stress_Level
- `train_model.py` - trains a RandomForestClassifier and saves `stress_model.joblib`
- `predict_and_export.py` - loads the model and dataset and writes `predicted_stress.txt` ("Faculty_ID Stress_Level" per line)
- `requirements.txt` - Python dependencies

How to run (Windows PowerShell)

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Generate dataset, train model, and export predictions:

```powershell
python generate_dataset.py
python train_model.py
python predict_and_export.py
```

The `predicted_stress.txt` file will be created in the same folder. Each line contains a Faculty ID and the predicted stress level (Low/Medium/High), which can be read by the Visual Prolog system.
