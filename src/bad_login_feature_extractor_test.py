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

if __name__ == '__main__':
  unittest.main()
