from record import Record
from collections import defaultdict
from operator import itemgetter
import heapq

class HostsFeatureExtractor:
  def __init__(self):
    self.hosts = defaultdict(lambda: 0)
    
  def add_record(self, r):
    """Adds a record to the feature extractor"""
    self.hosts[r.hostname] += 1
 
  def flush(self):
    # we want the large number with ties broken by the smallest string
    # Python likes to do all its sorts in the same direction,
    #   so we negate the number and they both end up with the same sort order
    return heapq.nsmallest(10, self.hosts.items(), key=lambda i: (-i[1], i[0]))

    