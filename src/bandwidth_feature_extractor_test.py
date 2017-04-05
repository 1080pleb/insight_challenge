import unittest
import record
from bandwidth_feature_extractor import BandwidthFeatureExtractor

class TestBandwidthFeatureExtractor(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = BandwidthFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        '/login',
        '/shuttle/countdown/',
        '/shuttle/countdown/liftoff.html'
    ])
    
  def test_larger_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log_test_100.txt')
    h = BandwidthFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertEqual(len(results), 10)


if __name__ == '__main__':
  unittest.main()
