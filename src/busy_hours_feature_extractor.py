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

class BusyHoursFeatureExtractor:
  def __init__(self):
    self.all_windows = []
    self.active_windows = []
    self.last_time = None
    
  def add_active_window(self, time):
    # checks if active window for this time already exists
    if self.active_windows and self.active_windows[-1].start_time >= time:
        return
    w = TimeWindow(time)
    self.all_windows.append(w)
    self.active_windows.append(w)

  def add_record(self, r):
    if self.last_time and self.last_time > r.timestamp:
      raise Exception('Event went back in time ' + str(r))
    if not self.last_time:
        self.last_time = r.timestamp
    
    # advancing windows up to current time stamp
    while self.last_time < r.timestamp:
        self.add_active_window(self.last_time)
        self.last_time += datetime.timedelta(seconds=1)
    # open window for current time
    self.add_active_window(self.last_time) 
     
    num_inactive_windows = 0
    for win in self.active_windows:
        if r.timestamp < win.start_time + datetime.timedelta(seconds=3600):
            win.count += 1
        else:
            num_inactive_windows += 1

    if  num_inactive_windows > 0:
        self.active_windows = self.active_windows[num_inactive_windows:]
 
  def flush(self):
    # we want 60min windows with most activity i.e. events
    # Python likes to do all its sorts in the same direction,
    # so we negate the number and they both end up with the same sort order:
    # smallest sort of negative window count but positive timestamp order
    time_tuples = [(tw.start_time, tw.count) for tw in self.all_windows]
    return heapq.nsmallest(10, time_tuples, key=lambda t: (-t[1], t[0]))

    