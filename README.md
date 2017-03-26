# homework

The program does following:
1. Reads config file "homework.cfg" 
1.a homework.cfg contains test cases 
1.b Each test case contain a URL and some data (string) which is expected to be present on HTML response

2. All methods are implemented in homework.py file.
2.a Requires following packages to be installed in order to run:
    2.a.1 import configparser
    2.a.2 import logging
    2.a.3 import re
    2.a.4 import requests
    
3. Actual script is monitor.py which read time_interval of scan in seconds from command-line.
USAGE Ex.:   python monitor.py  120  
This will scan all URL's specified in homework.cfg every 120 s.
The script also log the scan report as INFO or ERROR in monitor.log file.

4. I have provided sample cfg file and also a sample monitor.log file for reference.
    4.a homework.cfg provides example of how to write up test cases.
    4.b monitor.log provides example of how the log file looks like.
    




