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
            #self.protocol = command_parts[2]
        # command_parts[2] is usually the protocol (HTTP/1.0) but not all lines
        # have it and we don't need it anyway, so skip it.
