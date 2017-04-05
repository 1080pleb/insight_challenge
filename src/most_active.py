#Implement feature 1
import record
from busy_hours_feature_extractor import BusyHoursFeatureExtractor

records = record.read_from_file('log.txt')
print(len(records))
h = BusyHoursFeatureExtractor()
for r in records:
    h.add_record(r)

results = h.flush()
print(results)

