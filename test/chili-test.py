# Generated by Selenium IDE
import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import NoSuchElementException

class TestTest():

  def setup_method(self, method):
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument('--ignore-certificate-errors')
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homepage(self, add_nunit_attachment):
    self.driver.set_window_size(1440, 795)
    self.driver.get('http://127.0.0.1:8080') 
    self.driver.save_screenshot("test/home.png")
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "home.png")
    add_nunit_attachment(path, "home")

  def test_getstarted(self, add_nunit_attachment):
    self.driver.set_window_size(1440, 795)
    self.driver.get('http://127.0.0.1:8080') 
    self.driver.find_element(By.LINK_TEXT, "Get Started").click()
    self.driver.save_screenshot("test/getstarted.png")
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "getstarted.png")
    add_nunit_attachment(path, "getstarted")

  def test_blog(self, add_nunit_attachment):    
    self.driver.set_window_size(1440, 795)
    self.driver.get('http://127.0.0.1:8080') 
    self.driver.find_element(By.LINK_TEXT, "Blog").click()
    self.driver.save_screenshot("test/blog.png")
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "blog.png")
    add_nunit_attachment(path, "blog")

#  def test_samples(self, add_nunit_attachment):
#    try:
#        self.driver.set_window_size(1440, 795)
#        self.driver.get("https://maroon-chili-27bd3.netlify.app/")
#        elements = self.driver.find_elements(By.NAME, "sample")
#        assert elements == "sample"
#        self.driver.save_screenshot("test/sample.png")
#        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sample.png")
#        add_nunit_attachment(path, "sample")
#    except Exception as e:
#        raise



