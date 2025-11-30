import pandas as pd
from pathlib import Path
import joblib

BASE = Path(__file__).resolve().parent
CSV = BASE / 'faculty_workload.csv'
MODEL_IN = BASE / 'stress_model.joblib'
OUT_TXT = BASE / 'predicted_stress.txt'
OUT_FACTS = BASE / 'predicted_stress_facts.pl'
OUT_SWIREC = BASE / 'recommender_example.pl'

def load():
    df = pd.read_csv(CSV)
    return df

def predict_and_export():
    df = load()
    clf = joblib.load(MODEL_IN)
    features = ['Subjects_Handled','Students_Total','Prep_Hours','Research_Load_Hours','Committee_Duties','Admin_Tasks','Meeting_Hours','Sleep_Hours','Weekend_Work']
    preds = clf.predict(df[features])
    df['Predicted_Stress'] = preds
    # Write a simple text file: Faculty_ID Stress_Level
    with open(OUT_TXT, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            f.write(f"{row['Faculty_ID']} {row['Predicted_Stress']}\n")
    print(f"Wrote predictions for {len(df)} faculty to {OUT_TXT}")

    # Additionally write Prolog facts (classic Prolog syntax) for Visual Prolog / Prolog systems
    with open(OUT_FACTS, 'w', encoding='utf-8') as f:
        f.write('% Predicted stress facts: predicted_stress(FacultyID, Stress).\n')
        for _, row in df.iterrows():
            fid = str(row['Faculty_ID'])
            stress = str(row['Predicted_Stress'])
            # write atoms as quoted strings
            f.write(f"predicted_stress('{fid}','{stress}').\n")
    print(f"Wrote Prolog facts to {OUT_FACTS}")

    # Also write a small SWI-Prolog example recommender which reads the facts and prints recommendations.
    swicode = r"""
% recommender_example.pl -- load predicted_stress_facts.pl and produce recommendations
:- initialization(main).

recommendation('Low', ['Maintain current schedule', 'Monitor workload']).
recommendation('Medium', ['Prioritize tasks', 'Delegate where possible', 'Ensure 7+ hours sleep']).
recommendation('High', ['Reduce course load if possible', 'Request admin support', 'Schedule regular breaks', 'Seek wellness resources']).

main :-
    consult('predicted_stress_facts.pl'),
    forall(predicted_stress(F, S), (
        recommendation(S, Recs),
        format("~w: ~w -> Recommendations: ~w~n", [F, S, Recs])
    )),
    halt.
"""
    with open(OUT_SWIREC, 'w', encoding='utf-8') as f:
        f.write(swicode)
    print(f"Wrote SWI-Prolog example to {OUT_SWIREC}")

if __name__ == '__main__':
    predict_and_export()
