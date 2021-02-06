# Generated by Selenium IDE
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
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
vars = {}
  
driver.get("https://neat-birch-a5e6b.netlify.app/")
print('open_url')
driver.set_window_size(1440, 798)
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
print('clickhome')
driver.find_element(By.CSS_SELECTOR, ".navbar__list").click()
print('click_navlist')
driver.find_element(By.LINK_TEXT, "Blog").click()
print('click_blog')
driver.find_element(By.LINK_TEXT, "About").click()
print('click_about')
driver.find_element(By.LINK_TEXT, "Style Guide").click()
print('close')
  
driver.quit()
