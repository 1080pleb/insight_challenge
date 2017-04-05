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
    self.assertListEqual(results, [
        ("199.72.81.55", 6),
        ("burger.letters.com", 3),
        ("unicomp6.unicomp.net", 1)
    ])

  def test_larger_records_file(self):
    records = record.read_from_file('../insight_testsuite/tests/test_features/log_input/log_test_100.txt')
    h = HostsFeatureExtractor()
    for r in records:
      h.add_record(r)
    results = h.flush()
    self.assertListEqual(results, [
        ('ppp-mia-30.shadow.net', 6),
        ('205.189.154.54', 4),
        ('d104.aa.net', 4),
        ('unicomp6.unicomp.net', 4),
        ('199.120.110.21', 3),
        ('burger.letters.com', 3),
        ('129.94.144.152', 2),
        ('199.72.81.55', 2),
        ('ix-orl2-01.ix.netcom.com', 2),
        ('port26.annex2.nwlink.com', 2),
    ])
    
if __name__ == '__main__':
  unittest.main()
