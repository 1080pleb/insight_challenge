#Implement feature 1
import record
from busy_hours_feature_extractor import BusyHoursFeatureExtractor
from bad_login_feature_extractor import BadLoginFeatureExtractor
from bandwidth_feature_extractor import BandwidthFeatureExtractor 
from hosts_feature_extractor import HostsFeatureExtractor 
import time
import sys

# Stolen from http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

    # Print New Line on Complete
    if iteration == total: 
        print()

if len(sys.argv) < 6:
    # ./src/process_log.py log.txt hosts.txt hours.txt resources.txt blocked.txt
    print('Usage: %s <log> <hosts out> <hours out> <resources out> <blocked out>' % sys.argv[0])
    sys.exit(1)

input_log = sys.argv[1]
output_hosts = sys.argv[2]
output_hours = sys.argv[3]
output_resources = sys.argv[4]
output_blocked = sys.argv[5]

processed = 0
total = 4400644 # we cheated and know apriori
now = time.clock()

hours = BusyHoursFeatureExtractor()
hosts = HostsFeatureExtractor()
resources = BandwidthFeatureExtractor()
blocks = BadLoginFeatureExtractor()

with open(input_log, encoding="ISO-8859-1") as f:
  for line in f.readlines():
      # Handle progress bar
      if time.clock() - now > 1:
        print_progress(processed, total, suffix="%d/%d" % (processed, total))
        now = time.clock()
      processed += 1
      
      # Actually do the heavy lifting
      try:
          r = record.Record(line)
          hours.add_record(r)
          hosts.add_record(r)
          resources.add_record(r)
          blocks.add_record(r)
      except KeyboardInterrupt:
          raise
      except Exception as e:
          print(e)
          print('Error parsing line:', line)

results = h.flush()
print(results)
results = h.flush()
print(results)
results = h.flush()
print(results)
results = h.flush()
print(results)