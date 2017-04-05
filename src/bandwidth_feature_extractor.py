from record import Record
from collections import defaultdict
import heapq

class BandwidthFeatureExtractor:
  def __init__(self):
    self.resources = defaultdict(lambda: 0)
    
  def add_record(self, r):
    self.resources[r.resource] += r.bytes_transfered
 
  def flush(self):
    # we want resources by largest bandwidth with ties broken by the smallest string
    # Python likes to do all its sorts in the same direction,
    # so we negate the number and they both end up with the same sort order:
    # smallest sort of negative bandwidth but positive string
    return heapq.nsmallest(10, self.resources.keys(), key=lambda k: (-self.resources[k], k))