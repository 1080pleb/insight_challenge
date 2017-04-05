from record import Record
import datetime
from collections import defaultdict
from operator import itemgetter
import heapq

class TimeWindow:
  def __init__(self, time):
    self.start_time = time
    self.count = 0
    
  def __repr__(self):
    return "(%s, %s)" % (str(self.start_time), str(self.count))

class HostTracker:
  def __init__(self):
    self.active_windows = []
    self.block_until = None
    
  def add_active_window(self, time):
    # checks if active window for this time already exists
    if self.active_windows and self.active_windows[-1].start_time >= time:
        return
    self.active_windows.append(TimeWindow(time))

  def should_block(self, r):   
    if self.block_until and self.block_until > r.timestamp:
        return True

    # either block_until is None or time is outside current block_until
    # in which case we're done blocking
    self.block_until = None
    
    # we only care about logins
    if r.resource != '/login':
        return False
        
    if r.command == 'POST' and r.response_code == 200:
        # successful login!
        # therefore close all open windows
        self.active_windows = []
        return False
        
    self.add_active_window(r.timestamp)
    num_inactive_windows = 0
    
    # checks number of open windows for given time period (20s)
    print('ACTIVE WINDOWS', self.active_windows)
    for win in self.active_windows:
        if r.timestamp < win.start_time + datetime.timedelta(seconds=20):
            win.count += 1
            if win.count >= 3:
                self.block_until = r.timestamp + datetime.timedelta(seconds=300)
                self.active_windows = []
                # Do not block event that triggers block!
                return False
        else:
            num_inactive_windows += 1

    if  num_inactive_windows > 0:
        self.active_windows = self.active_windows[num_inactive_windows:]
    # nobody told us to block, so we allow
    return False

class BadLoginFeatureExtractor:
  def __init__(self):
    self.hosts = defaultdict(lambda:HostTracker())
    self.last_time = None
    self.blocked_records = []

  def add_record(self, r):
    print(r)
    if self.last_time and self.last_time > r.timestamp:
      raise Exception('Event went back in time ' + str(r))
    if not self.last_time:
        self.last_time = r.timestamp    
    if self.hosts[r.hostname].should_block(r):
        self.blocked_records.append(str(r))
 
  def flush(self):
    return self.blocked_records

    