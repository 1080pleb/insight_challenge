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

  def test_larger_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log_test_100.txt')
    h = BusyHoursFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:00:00:01 -0400'), 100),
        (record.parse_time('01/Jul/1995:00:00:02 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:03 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:04 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:05 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:06 -0400'), 99),
        (record.parse_time('01/Jul/1995:00:00:07 -0400'), 98),
        (record.parse_time('01/Jul/1995:00:00:08 -0400'), 98),
        (record.parse_time('01/Jul/1995:00:00:09 -0400'), 98),
        (record.parse_time('01/Jul/1995:00:00:10 -0400'), 93),
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

    h = BusyHoursFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        (record.parse_time('01/Jul/1995:23:31:12 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:13 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:14 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:15 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:16 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:17 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:18 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:19 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:20 -0400'), 3),
        (record.parse_time('01/Jul/1995:23:31:21 -0400'), 3),
    ])    
    
if __name__ == '__main__':
  unittest.main()
