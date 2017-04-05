import unittest
from record import Record
from datetime import datetime

class TestRecordParsing(unittest.TestCase):
    def test_r1(self):
        r = Record('199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245')
        self.assertEqual(r.hostname, '199.72.81.55')
        self.assertEqual(r.timestamp, datetime.strptime('01/Jul/1995:00:00:01 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        self.assertEqual(r.resource, '/history/apollo/')
        self.assertEqual(r.response_code, 200)
        self.assertEqual(r.bytes_transfered, 6245)

    def test_r2(self):
        r = Record('unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985')
        self.assertEqual(r.hostname, 'unicomp6.unicomp.net')
        self.assertEqual(r.timestamp, datetime.strptime('01/Jul/1995:00:00:06 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        self.assertEqual(r.resource, '/shuttle/countdown/')
        self.assertEqual(r.response_code, 200)
        self.assertEqual(r.bytes_transfered, 3985)
        
    def test_r3(self):
        r = Record('193.44.126.11 - - [04/Jul/1995:13:39:01 -0400] "GET /shuttle/missions/sts-71/news HTTP/1.0" 302 -')
        self.assertEqual(r.hostname, '193.44.126.11')
        self.assertEqual(r.timestamp, datetime.strptime('04/Jul/1995:13:39:01 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        self.assertEqual(r.resource, '/shuttle/missions/sts-71/news')
        self.assertEqual(r.response_code, 302)
        self.assertEqual(r.bytes_transfered, 0)        

    def test_r4(self):
        r = Record('klothos.crl.research.digital.com - - [10/Jul/1995:16:45:50 -0400] "" 400 -')
        self.assertEqual(r.hostname, 'klothos.crl.research.digital.com')
        self.assertEqual(r.timestamp, datetime.strptime('10/Jul/1995:16:45:50 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        #self.assertEqual(r.resource, '/shuttle/missions/sts-71/news')
        self.assertEqual(r.response_code, 400)
        self.assertEqual(r.bytes_transfered, 0)   

    def test_r5(self):
        r = Record('firewall.dfw.ibm.com - - [20/Jul/1995:07:34:34 -0400] "1/history/apollo/images/" 400 -')
        self.assertEqual(r.hostname, 'firewall.dfw.ibm.com')
        self.assertEqual(r.timestamp, datetime.strptime('20/Jul/1995:07:34:34 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        self.assertEqual(r.resource, '1/history/apollo/images/')
        self.assertEqual(r.response_code, 400)
        self.assertEqual(r.bytes_transfered, 0)           

    def test_r6(self):
        r = Record('128.159.122.20 - - [20/Jul/1995:15:28:50 -0400] "kĻtxĻtGĻt̓󢠴00 -')
        self.assertEqual(r.hostname, '128.159.122.20')
        self.assertEqual(r.timestamp, datetime.strptime('24/Jul/1995:13:52:50 -0400', '%d/%b/%Y:%H:%M:%S %z'))
        self.assertEqual(r.command, 'GET')
        #self.assertEqual(r.resource, '/shuttle/missions/sts-71/news')
        self.assertEqual(r.response_code, 302)
        self.assertEqual(r.bytes_transfered, 0)           
        
    def test_records_file(self):
        records = []
        with open('log_test.txt', encoding = "ISO-8859-1") as f:
            for line in f.readlines():
                try:
                    records.append(Record(line))
                except KeyboardInterrupt:
                    raise
                except:
                    self.fail('Failed to parse:\n' + line)
        self.assertEqual(len(records), 100)



if __name__ == '__main__':
    unittest.main()

