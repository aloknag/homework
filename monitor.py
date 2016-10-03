import homework
from sys import argv
import time


def probe():
    for test in test_cases:
        url, data = test['url'], test['data']
        message = 'Checking for %s' % url
        homework.log_to_file(logger, 'info', message)
        html, code, response_time = homework.request_url(url=url)
        if code == 200:
            # We got proper response for the web server
            if homework.match_data_in_html(html, data):
                message = "Request made to %s completed in %s time - '%s' was found" % (url, str(response_time), data)
                homework.log_to_file(logger, 'info', message)
            else:
                message = "Request made to %s completed in %s time - '%s' was *not* found" % (url, str(response_time), data)
                homework.log_to_file(logger, 'error', message)
        else:
            # Failed to reach the server and did not get any html data. SKIP/FAIL
            if code:
                # This means we have aa HTTP Error Code
                message = "Request made to %s failed with error code - %s" % (url, str(code))
                homework.log_to_file(logger, 'error', message)
            else:
                # Some other unknown connection error, DNS, Server timed-out, etc
                message = "Request made to %s failed - Connection Error" % url
                homework.log_to_file(logger, 'error', message)


if __name__ == '__main__':
    if len(argv) != 2:
        raise ValueError("Usage: python monitor.py <time in secs>")
    try:
        time_interval = float(argv[1])
    except ValueError:
        print "Time is a int value - Give a integer number"
        exit()
    # Read all test cases
    test_cases = homework.read_config()
    # Create aa logger for logging
    logger = homework.create_logger()
    while True:
        probe()
        time.sleep(time_interval)






