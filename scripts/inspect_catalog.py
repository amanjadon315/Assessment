from pathlib import Path
from collections import Counter
import json



BASE_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

print("=" * 60)
print("SHL CATALOG INSPECTION")
print("=" * 60)

print(f"Total Assessments : {len(catalog)}")


missing_descriptions = 0
missing_durations = 0
missing_languages = 0


job_level_counter = Counter()
key_counter = Counter()
remote_counter = Counter()
adaptive_counter = Counter()


for assessment in catalog:

    
    if not assessment.get("description"):
        missing_descriptions += 1

    
    if not assessment.get("duration"):
        missing_durations += 1

    
    if len(assessment.get("languages", [])) == 0:
        missing_languages += 1

    
    job_level_counter.update(assessment.get("job_levels", []))

    
    key_counter.update(assessment.get("keys", []))


    remote_counter.update([assessment.get("remote", "Unknown")])

    
    adaptive_counter.update([assessment.get("adaptive", "Unknown")])


print("\nMissing Data")
print("-" * 60)

print(f"Descriptions : {missing_descriptions}")
print(f"Durations    : {missing_durations}")
print(f"Languages    : {missing_languages}")

print("\nJob Levels")
print("-" * 60)

print(f"Unique Job Levels : {len(job_level_counter)}\n")

for level, count in job_level_counter.most_common():
    print(f"{level:<25} {count}")

print("\nAssessment Categories (Keys)")
print("-" * 60)

print(f"Unique Keys : {len(key_counter)}\n")

for key, count in key_counter.most_common():
    print(f"{key:<35} {count}")

print("\nRemote Distribution")
print("-" * 60)

for value, count in remote_counter.items():
    print(f"{value:<10} {count}")

print("\nAdaptive Distribution")
print("-" * 60)

for value, count in adaptive_counter.items():
    print(f"{value:<10} {count}")

print("\nInspection Complete.")