import unittest
import record
from bad_login_feature_extractor import BadLoginFeatureExtractor

class TestBadLoginFeatureExtractor(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = BadLoginFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        '199.72.81.55 - - [01/Jul/1995:00:00:13 -0400] "POST /login HTTP/1.0" 401 1420',
        '199.72.81.55 - - [01/Jul/1995:00:00:14 -0400] "POST /login HTTP/1.0" 401 1420',
        '199.72.81.55 - - [01/Jul/1995:00:00:15 -0400] "POST /login HTTP/1.0" 401 1420',
    ])
    
  def test_larger_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log_test_100.txt')
    h = BadLoginFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [])

  def test_overlapping_windows(self):
    records = [
        record.Record('f - - [01/Jul/1995:00:00:01 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:00:15 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:00:21 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:00:26 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:01:13 -0400] "GET /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:04:14 -0400] "POST /login HTTP/1.0" 402 0'),
        record.Record('f - - [02/Jul/1995:00:00:18 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:12 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:13 -0400] "GET /login HTTP/1.0" 200 0'),
        record.Record('f - - [02/Jul/1995:00:31:14 -0400] "POST /login HTTP/1.0" 401 0'),
    ]
    
    h = BadLoginFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        'f - - [01/Jul/1995:00:01:13 -0400] "GET /login HTTP/1.0" 401 0',
        'f - - [01/Jul/1995:00:04:14 -0400] "POST /login HTTP/1.0" 402 0',
        'f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0',
        'f - - [02/Jul/1995:00:31:12 -0400] "POST /login HTTP/1.0" 401 0',
        'f - - [02/Jul/1995:00:31:13 -0400] "GET /login HTTP/1.0" 200 0',
        'f - - [02/Jul/1995:00:31:14 -0400] "POST /login HTTP/1.0" 401 0',
    ])

  def test_diff_hosts(self):
    records = [
        record.Record('f - - [01/Jul/1995:00:00:01 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:00:15 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('e - - [01/Jul/1995:00:00:17 -0400] "POST /login HTTP/1.0" 401 0'), 
        record.Record('f - - [01/Jul/1995:00:00:21 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:00:26 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [01/Jul/1995:00:01:13 -0400] "GET /login HTTP/1.0" 401 0'),
        record.Record('e - - [01/Jul/1995:00:04:14 -0400] "POST /login HTTP/1.0" 402 0'),
        record.Record('f - - [02/Jul/1995:00:00:18 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('f - - [02/Jul/1995:00:31:12 -0400] "POST /login HTTP/1.0" 401 0'),
        record.Record('a - - [02/Jul/1995:00:31:13 -0400] "GET /login HTTP/1.0" 200 0'),
        record.Record('f - - [02/Jul/1995:00:31:14 -0400] "POST /login HTTP/1.0" 401 0'),
    ]
    
    h = BadLoginFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        'f - - [01/Jul/1995:00:01:13 -0400] "GET /login HTTP/1.0" 401 0',
        'f - - [02/Jul/1995:00:31:11 -0400] "POST /login HTTP/1.0" 401 0',
        'f - - [02/Jul/1995:00:31:12 -0400] "POST /login HTTP/1.0" 401 0',
        'f - - [02/Jul/1995:00:31:14 -0400] "POST /login HTTP/1.0" 401 0',
    ])
        
if __name__ == '__main__':
  unittest.main()
