class Record:
    def __init__(self, row):
        self.hostname = row.split()[0]
        self.timestamp = [x.strip('[') for x in row.split()[3]]
        self.command =  [x.strip('"') for x in row.split()[5]] # probably GET
        self.resource = row.split()[6]
        self.response_code = row.split()[8]
        self.bytes_transfered = row.split()[9]

