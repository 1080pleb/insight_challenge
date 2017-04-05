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
    print(results)
    self.assertListEqual(results, [
        'ppp-mia-30.shadow.net',
        '205.189.154.54',
        'd104.aa.net',
        'unicomp6.unicomp.net',
        '199.120.110.21',
        'burger.letters.com',
        '129.94.144.152',
        '199.72.81.55',
        'ix-orl2-01.ix.netcom.com',
        'port26.annex2.nwlink.com',
    ])
    

  def test_sort_order(self):
    r1 = record.Record('b - - [01/Jul/1995:00:00:11 -0400] "GET /b HTTP/1.0" 304 0')
    r2 = record.Record('c - - [01/Jul/1995:00:00:11 -0400] "GET /c HTTP/1.0" 304 0')
    r3 = record.Record('a - - [01/Jul/1995:00:00:11 -0400] "GET /a HTTP/1.0" 304 0')

    h = BandwidthFeatureExtractor()
    h.add_record(r1)
    h.add_record(r2)
    h.add_record(r3)
    self.assertListEqual(results, ['/a', '/b', '/c'])


if __name__ == '__main__':
  unittest.main()
