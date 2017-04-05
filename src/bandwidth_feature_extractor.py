from record import Record
from collections import defaultdict
import heapq

class BandwidthFeatureExtractor:
  def __init__(self):
    self.bandwidth_list = defaultdict(lambda: 0)
    
  def add_record(self, r):
    """Adds a record to the feature extractor"""
    self.bandwidth_list[r.resource] += r.bytes_transfered
 
  def flush(self):
    return self.bandwidth_list
    # dump 10 highest
    #top_10_hosts = heapq.nlargest(10, hostList)
    