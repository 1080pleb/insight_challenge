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
    self.assertDictEqual(results, {
        '/login': 8520,
        '/shuttle/countdown/': 7970,
        '/shuttle/countdown/liftoff.html': 0
    })

if __name__ == '__main__':
  unittest.main()
