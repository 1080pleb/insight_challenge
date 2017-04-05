from record import Record
from collections import defaultdict
import heapq

class BandwidthFeatureExtractor:
  def __init__(self):
    self.resources = defaultdict(lambda: 0)
    
  def add_record(self, r):
    self.resources[r.resource] += r.bytes_transfered
 
  def flush(self):
    # dump 10 highest
    print(heapq.nsmallest(10, self.resources.items(), key=lambda i: (-i[1], i[0])))
    return heapq.nlargest(10, self.resources.keys(), key=self.resources.__getitem__)