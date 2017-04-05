from datetime import datetime

TIME_FORMAT = '%d/%b/%Y:%H:%M:%S %z'

def parse_time(time_str):
  """Parses a time in the format provided by our logs."""
  return datetime.strptime(time_str, TIME_FORMAT)

class Record:
    def __init__(self, row):
        parts = row.split()
        self.hostname = parts[0]
        self.response_code = int(parts[-2])
        if parts[-1] == '-':
            self.bytes_transfered = 0
        else:
            self.bytes_transfered = int(parts[-1])

        time_str = row[row.find('[') + 1:row.find(']')]
        self.timestamp = parse_time(time_str)

        # commands_str should be of form "COMMAND RESOURCE PROTOCOL", but parts
        # of it can be missing, so we do a best effort parse.
        command_str = row[row.find('"') + 1:row.rfind('"')]
        command_parts = command_str.split()
        if len(command_parts) == 1:
            self.command = 'GET'
            self.resource = command_parts[0]
        elif len(command_parts) == 2:
            self.command = command_parts[0]
            self.resource = command_parts[1]
        else:
            self.command = command_parts[0]
            self.resource = command_parts[1]
            # part 3 is protocol but we don't care
    
    def __repr__(self):
      return '%s - - [%s] "%s %s HTTP/1.0" %s %s' % (self.hostname, self.timestamp.strftime(TIME_FORMAT), self.command, self.resource, self.response_code, self.bytes_transfered)

def read_from_file(filename):
  """Reads Records from a file line by line"""
  records = []
  with open(filename, encoding="ISO-8859-1") as f:
      for line in f.readlines():
          try:
              records.append(Record(line))
          except KeyboardInterrupt:
              raise
          except:
              print('Error parsing line:', line)
  return records
