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
    self.assertListEqual(results, [
    '/shuttle/countdown/count.gif',
    '/images/dual-pad.gif',
    '/',
    '/shuttle/missions/sts-70/images/KSC-95EC-1013.jpg',
    '/history/apollo/apollo-13/images/70HC314.GIF',
    '/shuttle/missions/sts-71/images/KSC-95EC-0882.jpg',
    '/shuttle/technology/sts-newsref/sts_asm.html',
    '/shuttle/missions/sts-71/images/KSC-95EC-0613.jpg',
    '/shuttle/missions/sts-71/movies/sts-71-mir-dock-2.mpg',
    '/shuttle/missions/sts-71/images/KSC-95EC-0912.gif'
    ])
    
  def test_sort_order(self):
    r1 = record.Record('b - - [01/Jul/1995:00:00:11 -0400] "GET /b HTTP/1.0" 304 0')
    r2 = record.Record('c - - [01/Jul/1995:00:00:11 -0400] "GET /c HTTP/1.0" 304 0')
    r3 = record.Record('a - - [01/Jul/1995:00:00:11 -0400] "GET /a HTTP/1.0" 304 0')

    h = BandwidthFeatureExtractor()
    h.add_record(r1)
    h.add_record(r2)
    h.add_record(r3)
    results = h.flush()
    self.assertListEqual(results, ['/a', '/b', '/c'])


if __name__ == '__main__':
  unittest.main()
