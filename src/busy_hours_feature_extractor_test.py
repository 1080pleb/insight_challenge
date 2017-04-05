import unittest
import record
from busy_hours_feature_extractor import BusyHoursFeatureExtractor

class TestBusyHoursFeatureExtractor(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = BusyHoursFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:00:00:01 -0400'), 10),
        (record.parse_time('01/Jul/1995:00:00:02 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:03 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:04 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:05 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:06 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:07 -0400'), 8),
        (record.parse_time('01/Jul/1995:00:00:08 -0400'), 8),
        (record.parse_time('01/Jul/1995:00:00:09 -0400'), 8),
        (record.parse_time('01/Jul/1995:00:00:10 -0400'), 7),
    ])

if __name__ == '__main__':
  unittest.main()
