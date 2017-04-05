from datetime import datetime

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
        self.timestamp = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S %z')

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

def read_from_file(filename):
  """Reads Records from a file line by line"""
  records = []
  with open(filename) as f:
      for line in f.readlines():
          try:
              records.append(Record(line))
          except KeyboardInterrupt:
              raise
          except:
              print('Error parsing line:', line)
  return records
