from record import Record
from collections import defaultdict
import heapq

class BandwidthFeatureExtractor:
  def __init__(self):
    self.bandwidth_list = defaultdict(lambda: 0)
    
  def add_record(self, r):
    """Adds a record to the feature extractor"""
    self.host_list[r.hostname] += 1
 
  def flush(self):
    return self.host_list
    # dump 10 highest
    #top_10_hosts = heapq.nlargest(10, hostList)
    