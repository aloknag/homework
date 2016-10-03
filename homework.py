import configparser
import logging
import re
import requests


def read_config():
    """Read the config file - named homework.cfg and returns a list of testcases"""
    config = configparser.ConfigParser()
    config.read('homework.cfg')

    def get_config_set(section):
        """Helper function getConfigSet"""
        return_dict = {}
        options = config.options(section=section)
        for option in options:
            try:
                return_dict[option] = config.get(section=section, option=option)
                if return_dict[option] == -1:
                    print 'skip: %s' % option
            except:
                print 'exception on %s' % option

        return return_dict

    configuration = map(get_config_set, config.sections())
    return configuration


def request_url(url=None):
    """Makes web request for the provided URL and returns HTML and Return-Code"""
    if not url:
        return None
    try:
        response = requests.get(url)
        html_data = response.text
        return_code = response.status_code
        time_taken = response.elapsed
    except:
        # Error in making request
        html_data = None
        return_code = None
        time_taken = None
    return html_data, return_code, time_taken


def match_data_in_html(html, data):
    """
    Input: html data and data to match in html
    Returns: True or False if match is found or otherwise
    """

    match = re.search(data, html)
    if match:
        # print 'Found', match.group()
        return True
    else:
        # print 'did not find'
        return False


def create_logger():
    """Create a logger instance and returns it for use"""
    logger = logging.getLogger('webmonitor')
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler('monitor.log')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def log_to_file(logger, level, message):
    "Write a message to log file using logger instance"
    if level == 'debug':
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.info("No message")

