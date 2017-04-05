import unittest
import record
from bandwidth_feature_extractor import BandwidthFeatureExtractor

class TestBandwidthFeatureExtractor(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = BandwidthFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = r.flush()
    self.assertDictEqual(results, {
        '/login': 1,
        '/shuttle/countdown/': 1,
        '/shuttle/countdown/liftoff.html': 1
    })

if __name__ == '__main__':
  unittest.main()
