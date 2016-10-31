import random
import time
from selenium import webdriver
import xml.etree.ElementTree as ET

from selenium.webdriver import chrome
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class FirefoxQuoraTest(unittest.TestCase):

    def setUp(self):
        PROXYList = ["203.66.159.44:3128", "31.207.0.99:3128", "219.255.197.90:3128", "64.103.27.184:8080",
                     "209.242.141.60:8080", "122.226.166.231:8080"]
        random.shuffle(PROXYList)
        PROXY = random.choice(PROXYList)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

        chrome = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)

        tree = ET.parse('values.xml')
        lst = tree.findall('links/link')
        for item in lst:
            browserlink = item.find('mylink').text
            chrome.get(browserlink)
            self.driver = chrome






    def test_login(self):



        signinbuttonXpath = "//div[@class='header_signin_with_search_bar action_button']"
        loginlinkXpath = "//a[text() = 'I Have a Quora Account']"
        loginFieldXpath = "//form/div[1]/div[1]/input"
        passworFieldXpath = "//form/div[1]/div[2]/input"
        loginbuttonXpath = "//input[@value='Login']"
        tree = ET.parse('values.xml')
        root = tree.getroot()
        lst = tree.findall('users/user')

        for item in lst:

            time.sleep(2)
            signinbutttonElement = driver.find_element_by_xpath(signinbuttonXpath)
            signinbutttonElement.click()
            time.sleep(5)
            loginlinkElement = webdriver.find_element_by_xpath(loginlinkXpath)
            loginlinkElement.click()
            time.sleep(2)
            emailvalue = item.find('email').text
            loginFieldElement = webdriver.find_element_by_xpath(loginFieldXpath)
            time.sleep(5)
            loginFieldElement.click()
            loginFieldElement.clear()
            loginFieldElement.send_keys(emailvalue)
            passvalue = item.find('password').text
            passwordFieldElement = webdriver.find_element_by_xpath(passworFieldXpath)
            passwordFieldElement.clear()
            passwordFieldElement.send_keys(passvalue)
            loginbuttonElement = webdriver.find_element_by_xpath(loginbuttonXpath)
            time.sleep(20)
            loginbuttonElement.click()
            time.sleep(10)

