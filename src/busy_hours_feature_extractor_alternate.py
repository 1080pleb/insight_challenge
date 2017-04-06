from record import Record
from collections import defaultdict, deque
from operator import itemgetter
import heapq

HOUR = 3600


class TimeWindow:

    def __init__(self, time):
        self.start_time = time
        self.count = 0

    def __repr__(self):
        return "(%s, %s)" % (str(self.start_time), str(self.count))

    # define custom less-than operator
    # to use directly in heaps
    def __lt__(lhs, rhs):
        if lhs.count == rhs.count:
            # we want highest timestamps last
            return lhs.start_time > rhs.start_time
        return lhs.count < rhs.count


class BusyHoursFeatureExtractorAlternate:

    def __init__(self):
        self.best_windows = []
        self.active_windows = deque()
        self.last_time = None

    def add_active_window(self, time):
        # checks if active window for this time already exists
        if self.active_windows and self.active_windows[-1].start_time >= time:
            return
        self.active_windows.append(TimeWindow(time))

    def retire_active_windows(self, num_inactive_windows):
        for i in range(num_inactive_windows):
            win = self.active_windows.popleft()
            # if don't have 10 windows yet, add to heap
            if len(self.best_windows) < 10:
                heapq.heappush(self.best_windows, win)
            # if already have 10 best, replace only if better
            elif self.best_windows[0] < win:
                heapq.heappushpop(self.best_windows, win)

    def add_record(self, r):
        if self.last_time and self.last_time > r.timestamp:
            raise Exception('Event went back in time ' + str(r))
        self.last_time = r.timestamp
        self.add_active_window(r.timestamp)

        num_inactive_windows = 0
        oldest_acceptable_window = r.timestamp - HOUR
        for win in self.active_windows:
            if oldest_acceptable_window < win.start_time:
                win.count += 1
            else:
                num_inactive_windows += 1

        self.retire_active_windows(num_inactive_windows)

    def flush(self):
        # we want 60min windows with most activity i.e. events
        # Python likes to do all its sorts in the same direction,
        # so we negate the number and they both end up with the same sort order:
        # smallest sort of negative window count but positive timestamp order
        self.retire_active_windows(len(self.active_windows))
        self.best_windows.sort(reverse=True)
        return [(tw.start_time, tw.count) for tw in self.best_windows]


