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


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
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
print('click_style')
driver.find_element(By.LINK_TEXT, "Features").click()
element = driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .btn")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .btn")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .btn")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
print('close')
  
driver.quit()
