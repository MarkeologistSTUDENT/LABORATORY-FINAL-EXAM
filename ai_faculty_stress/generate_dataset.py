import csv
import random
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
CSV_PATH = OUT_DIR / "faculty_workload.csv"

def points_subjects(n):
    if n <= 2:
        return 1
    if 3 <= n <= 4:
        return 2
    return 3

def points_students(n):
    if n < 60:
        return 1
    if 60 <= n <= 100:
        return 2
    return 3

def points_prep(h):
    if h < 6:
        return 1
    if 6 <= h <= 10:
        return 2
    return 3

def points_research(h):
    if h < 4:
        return 1
    if 4 <= h <= 6:
        return 2
    return 3

def points_committee(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return 3

def points_admin(n):
    if n <= 1:
        return 1
    if 2 <= n <= 3:
        return 2
    return 3

def points_meet(h):
    if h < 3:
        return 1
    if 3 <= h <= 6:
        return 2
    return 3

def points_sleep(h):
    if h >= 7:
        return 1
    if h == 6:
        return 2
    return 3

def points_weekend(n):
    if n == 0:
        return 1
    if 1 <= n <= 2:
        return 2
    return 3

def compute_wss(row):
    pts = 0
    pts += points_subjects(int(row['Subjects_Handled']))
    pts += points_students(int(row['Students_Total']))
    pts += points_prep(int(row['Prep_Hours']))
    pts += points_research(int(row['Research_Load_Hours']))
    pts += points_committee(int(row['Committee_Duties']))
    pts += points_admin(int(row['Admin_Tasks']))
    pts += points_meet(int(row['Meeting_Hours']))
    pts += points_sleep(int(row['Sleep_Hours']))
    pts += points_weekend(int(row['Weekend_Work']))
    return pts

def wss_to_label(wss):
    if 9 <= wss <= 14:
        return 'Low'
    if 15 <= wss <= 20:
        return 'Medium'
    return 'High'

def generate_row(fid_idx):
    # Reasonable ranges based on spec
    subjects = random.choices([1,2,3,4,5,6], weights=[5,10,40,30,10,5])[0]
    students = int(subjects * random.randint(20,35))
    prep = max(1, int(random.gauss(8,3)))
    research = max(0, int(random.gauss(4,2)))
    committee = random.choices([0,1,2,3,4], weights=[30,40,20,7,3])[0]
    admin = random.choices([0,1,2,3,4,5], weights=[30,40,15,10,3,2])[0]
    meeting = max(0, int(random.gauss(4,2)))
    sleep = max(3, min(9, int(random.gauss(6.8,1))))
    weekend = random.choices([0,1,2,3,4], weights=[40,35,15,8,2])[0]
    fid = f"F{fid_idx:03d}"
    row = {
        'Faculty_ID': fid,
        'Subjects_Handled': subjects,
        'Students_Total': students,
        'Prep_Hours': prep,
        'Research_Load_Hours': research,
        'Committee_Duties': committee,
        'Admin_Tasks': admin,
        'Meeting_Hours': meeting,
        'Sleep_Hours': sleep,
        'Weekend_Work': weekend,
    }
    wss = compute_wss(row)
    row['WSS'] = wss
    row['Stress_Level'] = wss_to_label(wss)
    return row

def generate_dataset(n=250):
    rows = []
    for i in range(1, n+1):
        rows.append(generate_row(i))
    return rows

def save_csv(rows, path=CSV_PATH):
    fieldnames = ['Faculty_ID','Subjects_Handled','Students_Total','Prep_Hours','Research_Load_Hours','Committee_Duties','Admin_Tasks','Meeting_Hours','Sleep_Hours','Weekend_Work','WSS','Stress_Level']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"Saved {len(rows)} rows to {path}")

if __name__ == '__main__':
    rows = generate_dataset(250)
    save_csv(rows)
