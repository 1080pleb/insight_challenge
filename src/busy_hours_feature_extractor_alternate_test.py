import unittest
import record
from busy_hours_feature_extractor_alternate import BusyHoursFeatureExtractorAlternate

class TestBusyHoursFeatureExtractorAlternate(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = BusyHoursFeatureExtractorAlternate()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:00:00:01 -0400'), 10),
        (record.parse_time('01/Jul/1995:00:00:06 -0400'), 9),
        (record.parse_time('01/Jul/1995:00:00:09 -0400'), 8),
        (record.parse_time('01/Jul/1995:00:00:11 -0400'), 7),
        (record.parse_time('01/Jul/1995:00:00:12 -0400'), 6),
        (record.parse_time('01/Jul/1995:00:00:13 -0400'), 5),
        (record.parse_time('01/Jul/1995:00:00:14 -0400'), 4),
        (record.parse_time('01/Jul/1995:00:00:15 -0400'), 2),
        ])

  def test_larger_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log_test_100.txt')
    h = BusyHoursFeatureExtractorAlternate()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:00:00:01 -0400'), 100),
        (record.parse_time('01/Jul/1995:00:00:06 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:09 -0400'), 98),
        (record.parse_time('01/Jul/1995:00:00:11 -0400'), 93),
        (record.parse_time('01/Jul/1995:00:00:12 -0400'), 91),
        (record.parse_time('01/Jul/1995:00:00:13 -0400'), 84),
        (record.parse_time('01/Jul/1995:00:00:14 -0400'), 78),
        (record.parse_time('01/Jul/1995:00:00:15 -0400'), 71),
        (record.parse_time('01/Jul/1995:00:00:17 -0400'), 64),
        (record.parse_time('01/Jul/1995:00:00:18 -0400'), 58),
        ])
    
  def test_window_closing(self):
    records = [
        record.Record('b - - [01/Jul/1995:00:00:11 -0400] "GET /b HTTP/1.0" 304 0'),
        record.Record('c - - [01/Jul/1995:00:00:12 -0400] "GET /c HTTP/1.0" 304 0'),
        record.Record('a - - [01/Jul/1995:23:43:11 -0400] "GET /a HTTP/1.0" 304 0'),
        record.Record('d - - [02/Jul/1995:00:00:12 -0400] "GET /b HTTP/1.0" 304 0'),
        record.Record('e - - [02/Jul/1995:00:31:11 -0400] "GET /c HTTP/1.0" 304 0'),
        record.Record('f - - [04/Jul/1995:00:00:11 -0400] "GET /a HTTP/1.0" 304 0'),
    ]

    h = BusyHoursFeatureExtractorAlternate()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:23:43:11 -0400'), 3),
        (record.parse_time('01/Jul/1995:00:00:11 -0400'), 2),
        (record.parse_time('02/Jul/1995:00:00:12 -0400'), 2),
        (record.parse_time('01/Jul/1995:00:00:12 -0400'), 1),
        (record.parse_time('02/Jul/1995:00:31:11 -0400'), 1),
        (record.parse_time('04/Jul/1995:00:00:11 -0400'), 1),
    ])    
    
if __name__ == '__main__':
  unittest.main()
