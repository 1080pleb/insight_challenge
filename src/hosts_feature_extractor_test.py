import unittest
import record
from hosts_feature_extractor import HostsFeatureExtractor

class TestHostsFeatureExtractor(unittest.TestCase):
  def test_provided_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log.txt')
    h = HostsFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertDictEqual(results, {
        "199.72.81.55": 6,
        "burger.letters.com": 3,
        "unicomp6.unicomp.net": 1
    })

if __name__ == '__main__':
  unittest.main()
