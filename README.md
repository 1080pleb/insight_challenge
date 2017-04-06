The main driver is process_log.py

The input file is parsed via record.py into Record objects. Records are passed
to each of the four Feature Extractors which use the parts they need. Feature
Extractors have a incremental interface so they could be passed live log data.
They have a flush method to produce final results.

Bad Login Feature Extractor currently produces all logs at flush time, but could
be made to issue blocks incrementally with a minor change. This was done for
consistency with the other Feature Extractors.

Busy Hours Feature Extractor, because it opens windows for every second, tends to
produce a cluster of overlapping windows. The Alternate version only opens windows
when events arrive leading to a broader distribtuion of traffic-dense periods.

On a reasonable machine, this processes approximately 2000 records per second.
Project is written using python3.
It was tested on a windows 7 machine (Python version 3.6.0), a macbook
pro (version 3.5.1), and a linux machine (version 3.4.3).

Contact info:
jpnmitchell@gmail.com
609.240.4129