from __future__ import print_function
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Test Case Base Class (to be inherited by all Tests)
class BaseTest(unittest.TestCase):
    """ Base test class for all tests """

    TOTAL_TESTS = 0

    @classmethod
    def setUpClass(cls):
        firefox_loc = "/usr/bin/firefox"
        firefox_binary = FirefoxBinary(firefox_loc)
        capability = DesiredCapabilities.FIREFOX.copy()
        #
        capability['loggingPrefs'] = {
            'driver': 'WARNING',
            'server': 'ALL',
            'client': 'ALL',
            'performance': 'ALL',
            'browser': 'SEVERE'}
        #
        # Initiate a Firefox Browser-based Test run
        #

        cls._browser = webdriver.Firefox(
            firefox_binary=firefox_binary,
            capabilities=capability
        )
        cls._browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        if cls._browser is not None:
            cls._browser.quit()
