#Implement feature 1
import unittest
from record import Record

records = []

with open('log_test2.txt', encoding = "ISO-8859-1") as f:
    for line in f.readlines():
        try:
            records.append(Record(line))
        except KeyboardInterrupt:
            raise
        except:
            print('Error parsing line:', line)
print(len(records))
print(records)
#hostList = {}

#for entry in records:
#    if entry[0] == self.hostname:
        

#not up to date
