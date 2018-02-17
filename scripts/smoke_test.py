#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :
""" Unittest for Selenium """
import unittest
import os
from selenium import webdriver


class PuppetWebappSmokeTest(unittest.TestCase):
    """ Class for testing PuppetWebapp """
    def setUp(self):
        executor = "http://%s:4444/wd/hub" % (os.environ.get('SEL_HOST'))
        self.driver = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            command_executor=executor
        )
        self.driver.get(os.environ.get('APP_URL'))

    def test_root_page(self):
        """ Fire-up driver and test """
        driver = self.driver
        assert "Version Number:" in str(driver.page_source)

    def test_root_page_images(self):
        """ Fire-up driver and test """
        driver = self.driver
        images = driver.find_elements_by_tag_name('img')
        assert images != []

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
